#!/usr/bin/env python3
"""canon_deploy.py — раскладка флот-канона (вариант A).
Источник: ventures/canon/ (skills/** + MANIFEST.json). Копии в профилях не правятся.
Режимы: (без аргументов) --deploy | --check | --update-manifest
"""
import argparse, hashlib, json, os, shutil, sys, time

CANON = os.path.dirname(os.path.realpath(__file__))
MANIFEST = os.path.join(CANON, "MANIFEST.json")
AUDIT = os.path.join(CANON, "audit.log")
H = os.path.realpath(os.environ.get("LOCALAPPDATA", "") + "/hermes") or os.path.expanduser("~/AppData/Local/hermes")

def target_root(name):
    return os.path.join(H, "skills") if name == "default" else os.path.join(H, "profiles", name, "skills")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def log(msg):
    with open(AUDIT, "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")

def load():
    m = json.load(open(MANIFEST, encoding="utf-8"))
    for it in m["items"]:
        cp = os.path.join(CANON, it["relpath"])
        assert os.path.isfile(cp), f"канон-файл отсутствует: {it['relpath']}"
        assert sha(cp) == it["sha256"], f"канон-файл расходится с манифестом: {it['relpath']} (запусти --update-manifest)"
    return m

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true"); ap.add_argument("--deploy", action="store_true")
    ap.add_argument("--update-manifest", action="store_true")
    a = ap.parse_args()
    if a.update_manifest:
        m = json.load(open(MANIFEST, encoding="utf-8")) if os.path.isfile(MANIFEST) else {"items": []}
        for it in list(m["items"]):
            if not os.path.isfile(os.path.join(CANON, it["relpath"])):
                m["items"].remove(it); log(f"removed-from-manifest {it['relpath']}")
        for root, dirs, files in os.walk(os.path.join(CANON, "skills")):
            for f in files:
                rel = os.path.relpath(os.path.join(root, f), CANON).replace("\\", "/")
                if not any(i["relpath"] == rel for i in m["items"]):
                    m["items"].append({"relpath": rel, "sha256": "", "targets": [], "added": time.strftime("%Y-%m-%d")}); log(f"added-to-manifest {rel}")
        for it in m["items"]:
            it["sha256"] = sha(os.path.join(CANON, it["relpath"]))
        json.dump(m, open(MANIFEST, "w", encoding="utf-8"), ensure_ascii=False, indent=1); log("manifest-updated")
        print("manifest updated:", len(m["items"]), "items"); return 0
    m = load(); drift = []
    for it in m["items"]:
        cp = os.path.join(CANON, it["relpath"])
        for t in it["targets"]:
            dst = os.path.join(target_root(t), *it["relpath"].split("/")[1:])
            if not os.path.isfile(dst) or sha(dst) != it["sha256"]:
                drift.append((it["relpath"], t, "missing" if not os.path.isfile(dst) else "changed"))
    if a.check:
        for rel, t, kind in drift: print(f"DRIFT {kind}: {t}:{rel}")
        print(f"check: {len(drift)} drift / {len(m['items'])} items")
        log(f"check drift={len(drift)}")
        return 1 if drift else 0
    for it in m["items"]:
        cp = os.path.join(CANON, it["relpath"])
        for t in it["targets"]:
            dst = os.path.join(target_root(t), *it["relpath"].split("/")[1:])
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(cp, dst)
    for rel, t, kind in drift: log(f"repaired {kind} {t}:{rel}")
    log(f"deploy items={len(m['items'])} repaired={len(drift)}")
    print(f"deploy: {len(m['items'])} items, repaired {len(drift)}"); return 0

if __name__ == "__main__":
    sys.exit(main())
