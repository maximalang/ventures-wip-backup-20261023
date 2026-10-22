# Рынок LLM-провайдеров и релеев
> retrieved_at: 2026-10-22 · Источник прохода: `docs/fleet-ops/provider-market-research-20261022/` (таблица 28 кандидатов `all-candidates-table.md`, курс `fx-usd-rub.json`, acceptance-чек). Все цены — snapshot на 22.10.2026, горизонт свежести 14 дней.

## Source facts (verified — сверено с таблицей 22.10)
- **Эталоны вендоров**: Anthropic Opus 5.5 $4/$20 per M, Sonnet 5.5 $2/$10 — [retrieved 2026-10-22, verified, platform.claude.com/docs/en/about-claude/pricing]
- **Z.ai GLM-5.3**: $1.40/$4.40 per M, cached $0.26 — [retrieved 2026-10-22, verified, docs.z.ai/guides/overview/pricing]
- **NanoGPT** (🟢 пилот №1): Opus 5.5 $4/$20 = официальной; **GLM-5.3 $0.60/$1.10 — ниже официальной**; pinning upstream + `allow_fallbacks:false` для GLM; вход от $0.10 крипто; для Opus pinning недоступен — [retrieved 2026-10-22, verified, nano-gpt.com/pricing]
- **AIHubMix** (🟢): цена = официальной (Opus $4/$20, GLM-5.3 $1.13/$3.94); жалоба на governance 24.08.2026 — [retrieved 2026-10-22, verified, aihubmix.com llms.txt]
- **PackyAPI** (🟡): самая низкая нормализованная цена (Opus $0.46/$2.29); валюта списания не подтверждена без checkout — [retrieved 2026-10-22, verified, packyapi.com/pricing]
- **UnoRouter** (🟡): −78% на Opus ($0.89/$4.47 PAYG); единственный зафиксированный случай подмены (зонд-конкурент, n=1) — [retrieved 2026-10-22, verified, unorouter.com/en/pricing]
- **LMU AI** (🟡): C-PRO self-disclosed reverse-пул, ¥599/30д ≈ −83.5%; privacy policy в Draft — [retrieved 2026-10-22, verified, api.lmuai.ai]
- **Baseline не-«серые»**: DeepInfra GLM-5.3: промо $0.563 in / $2.50 out, cached input $0.125; обычный (непромо) тариф $0.90/$4.00 (cached $0.20); Flex (0.8×) $0.45/$2.00 — перепроверка тиком 19:57 22.10: изменения цен против утреннего snapshot НЕТ (sha-триггер noise; cached-цены дозаписаны) — [retrieved 2026-10-22, verified, deepinfra.com/zai-org/GLM-5.3]; Chutes TEE: GLM-5.2 $1.25/$3.95, Kimi-K3 $1.85/$9.50 (GLM-5.3 нет) — [retrieved 2026-10-22, verified]
- FX-пересчёт ₽→$ по ЦБ **81.9739** на 22.10.2026 (пред. 82.8879) — [retrieved 2026-10-22, verified, cbr-xml-daily.ru]
- plakcel — подтверждённая подмена (234 имени = 1 Qwen3-бэкенд); политика владельца 21.10: аккуратно, не удалять — [fact_store #25]

## Выводы (не source facts)
- Финалисты прохода 22.10 (acceptance-check): PackyAPI, LMU AI, AIHubMix, UnoRouter, NanoGPT, NeuroAPI — confidence medium (критерии отбора в отчёте).
- Собственных платных API-тестов не проводилось (0) — все цены со страниц провайдеров, не из живых вызовов.

## Unknowns / watch
- Живой pinning-тест NanoGPT (attribution upstream) — не проведён.
- ChatAnywhere «95/100 n=27» — первоисточник не загружен (pending).
- POLOAPI: жалоба linux.do не перепроверена (pending).

## История обновлений
- 2026-10-22 (тик 19:57, domain-watch) — sha-триггеры deepinfra/nano-gpt: цены GLM-5.3 неизменны (noise); дозаписаны cached/непромо/Flex-цены DeepInfra.
- 2026-10-22 — первичное наполнение; исправлена неточность v1 (NanoGPT: Opus=официалу, GLM ниже официала). Артефакт: provider-market-research-20261022.
