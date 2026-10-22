# Рынок LLM-провайдеров и релеев
> Последнее обновление: 2026-10-22 · Источники последнего прохода: `docs/fleet-ops/provider-market-research-20261022/` (28 кандидатов, все цены с URL)

## Ключевые факты (проверенные)
- **Эталоны вендоров**: Anthropic Opus 5.5 $4/$20 per M, Sonnet 5.5 $2/$10; Z.ai GLM-5.3 $1.40/$4.40 (cached $0.26) — [2026-10-22, high, официальные страницы pricing]
- **NanoGPT** — 🟢 пилот №1: цены = официалу, pinning upstream + `allow_fallbacks:false`, attribution есть; вход от $0.10 крипто — [2026-10-22, high, nano-gpt.com/pricing]
- **AIHubMix** — цена = официальной, лучшее схождение технических сигналов; жалоба на governance 24.08.2026 — [2026-10-22, medium, aihubmix llms.txt]
- **PackyAPI** — самая низкая нормализованная цена (Opus $0.46/M), но валюта списания не подтверждена, слабый репутационный профиль — [2026-10-22, medium]
- **UnoRouter** — −78% на Opus, но единственный зафиксированный случай подмены (n=1, зонд-конкурент) — [2026-10-22, medium]
- **LMU AI** — self-disclosed reverse-пул C-PRO (¥599/30д ≈ −83.5%), privacy policy в Draft — [2026-10-22, high, self-disclosure]
- **Baseline не-«серые»**: DeepInfra GLM-5.3 $0.563/$2.50 promo; Chutes TEE: GLM-5.2 $1.25/$3.95, Kimi-K3 $1.85/$9.50 — [2026-10-22, high]
- **plakcel** — подтверждённая подмена (234 имени = 1 Qwen3-бэкенд); политика владельца 21.10: аккуратно, НЕ удалять — [fact #25]
- FX-пересчёт ₽→$ по ЦБ **81.9739** на 22.10.2026; собственных платных API-тестов не проводилось — [2026-10-22, high]

## Открытые вопросы / watch
- Живой pinning-тест NanoGPT (attribution upstream) — не проведён.
- ChatAnywhere «95/100 n=27» — первоисточник не загружен.
- POLOAPI: жалоба linux.do не перепроверена.

## История обновлений
- 2026-10-22 — первичное наполнение из `docs/fleet-ops/provider-market-research-20261022/` (полная таблица 28 кандидатов: `all-candidates-table.md`).
