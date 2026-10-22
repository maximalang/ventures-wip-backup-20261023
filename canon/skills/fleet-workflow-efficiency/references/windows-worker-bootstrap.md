# Incident: Windows managed-worker bootstrap wedge (t_d4350193)

Дата: 2026-10-20..22 · Статус: закрыт end-to-end (run 5428)

## Симптом
Каждый kanban-воркер (qa/research/design) с 20.10 вис на bootstrap: CPU 0.0%, убивался только managed_worker_ready_timeout (+300с). 6+ ранов (5417–5427), сирот не оставалось благодаря lifecycle-фиксу t_422a073a.

## Диагностика
- Полный нативный py-spy дамп (8 нитей, `scratch/native-dumps.txt`): главный поток в init numpy/OpenBLAS (LoadLibrary → DllMain под loader-lock) ждёт critical section; фоновые ридеры (stdin-frames/websocket/runtime-store) припаркованы на сокетах.
- Прямой импорт numpy из того же env-venv — 0.3с; standalone-репро с parked-threads + below-normal приоритетом — 0.1с (4/4). Значит «нити читателей сами по себе» — не доказанная причина.
- `OPENBLAS_NUM_THREADS=1` подтверждён в среде ребёнка — НЕ устранил wedge (канарейка 5426).
- Точный механизм — гипотеза по стекам (загрузка DLL внутри plugin-loader'а в момент, когда фоновые нити уже живут).

## Фикс (эмпирический контракт)
Прогрев numpy в теле модуля `agent/managed_worker.py` — до старта reader-нитей; повторный импорт плагином идёт из `sys.modules` без загрузки DLL. Пин `OPENBLAS_NUM_THREADS=1` (setdefault) оставлен.

Коммиты: c857f8056ee (lifecycle) → e64fc0e3756 (prewarm) → fcdd4d54f30 (тесты) → 3b4ed9e65a9 (provenance-пин проб). Форк: fix/kanban-managed-worker-zombies @ 52c8bed4402.

## Верификация
- Run 5428: spawn 18:58:13 → первый heartbeat +16с → completed 19:13:02, exit 0, сирот нет, артефакт QA-SENTINEL-MIXED-MODULES-MATRIX.md.
- Тесты: subprocess-пробы со stub-numpy (число нитей при прогреве = 1, пин до импорта, сохранение явного значения, provenance = тестируемый checkout); отрицательный контроль: без prewarm проба падает. Набор lifecycle: 107 passed / 0 failed / 8 skipped.

## Уроки
- Зависание на импорте → py-spy native dump, не пересоздание окружения: окружения не пересоздаются (generations+leases переиспользуются).
- Heartbeat/quota — не прогресс; доказательство = артефакт + терминальное событие run.
- Утечка lease-файлов (`.leases` — скрытый каталог в каждом окружении, 889 файлов, 279 >24ч на 22.10) — штатный уборщик не идентифицирован; удалять по возрасту без проверки владельца нельзя.
