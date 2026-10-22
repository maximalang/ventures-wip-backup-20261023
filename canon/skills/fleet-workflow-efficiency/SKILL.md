---
name: fleet-workflow-efficiency
description: "Use when checking native fleet routing or handoffs."
---

# Совместимость: один workflow

Основной контракт исполнения — `company-os`; не загружай второй стандарт по этому имени.

Для конкретного сбоя Hermes используй `hermes-agent` и официальный контракт установленной версии: один dispatcher, один task/run на deliverable, native dependency/review/recovery, неизменные money/access/irreversibility gates. Quota/heartbeat/status не являются полезным прогрессом.

Перед recovery проверь точный target, артефакт и последний исход; после — фактический native статус и продолжение. Не вводи launchers/watchdogs/новые receipts и не обходи deny другим путём. Подробности прошлых инцидентов хранятся вне загружаемого skill.

## Уроки инцидентов

Гипотеза → ограниченный эксперимент → результат/артефакт; heartbeat/quota ≠ прогресс; переустановка окружения только при подтверждённой необходимости (generations+leases переиспользуются). Пример: bootstrap-дедлок воркеров на импорте numpy/OpenBLAS закрыт прогревом в теле `agent/managed_worker.py` до старта reader-нитей (`OPENBLAS_NUM_THREADS` один не лечит); при зависании на импорте — py-spy native dump, не пересоздание env. Детали и коммиты: references/windows-worker-bootstrap.md.
