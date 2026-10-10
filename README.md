# Planets

Подготовленная среда для поиска транзитоподобных сигналов в открытых данных TESS.
Исследование ещё не начато: реальные FITS не загружены, кандидатов и открытий нет.

Первый этап — пилот на **20–50 звёздах**. Основной агент управляет;
GPT-6 Luna выполняет исследования: `low` для простых задач, `xhigh` для сложных.

Начни следующий чат с [docs/NEXT_CHAT.md](docs/NEXT_CHAT.md).
Методология, источники и ограничения — в [docs/RESEARCH_PLAN.md](docs/RESEARCH_PLAN.md).

## Локальное окружение

Нужны Python 3.11 и `uv`. В текущем проекте `.venv` уже подготовлено.

```powershell
uv venv --python 3.11 .venv
uv pip sync --python .venv/Scripts/python.exe requirements.txt
.venv\Scripts\python.exe scripts\check_environment.py
```

Без `uv`: `py -3.11 -m venv .venv`, затем
`.venv\Scripts\python.exe -m pip install -r requirements.txt`.
`requirements.in` перечисляет прямые зависимости, `requirements.txt` фиксирует версии.
Проверка без сети восстанавливает искусственный транзит BLS и проверяет настройки.
Она не подтверждает доступ к MAST или работоспособность на реальных наблюдениях.
Lightkurve сообщает о необязательном `tpfmodel` без `oktopus`: PRF-моделирование
не подготовлено; BLS и обычная апертурная фотометрия не требуют этого дополнения.

## Готовность к исследованию

Подготовлены окружение, инструкции, параметры пилота и offline smoke check.
Автоматический конвейер отбора целей, загрузки и научного веттинга пока не реализован:
его минимальную версию Luna подготовит в исследовательском чате и проверит на контролях.
`config/pilot.toml` содержит начальные параметры и лимиты, а не универсальную методику.

`data/`, `research_outputs/`, `.venv/` и `.cache/` локальные и исключены из Git.
Для каждого запуска сохранять манифест входов, версии, параметры, checkpoint и отчёт.
Исходные наблюдения сохраняются неизменными; связь с результатами — через SHA-256.
Публикация результатов кандидатов требует отдельного разрешения.

See [AGENTS.md](AGENTS.md) for contributor guidelines.

## Clone

```sh
git clone --recurse-submodules https://github.com/Evgen-rus/Planets.git
```

For an existing checkout, run `git submodule update --init --recursive`.

## Project-local Codex workflow

The `dev-agent-workflow` skill is pinned as a submodule at
`.agents/skills/dev-agent-workflow`. Its four Codex agent templates are tracked
in `.codex/agents/`, with research instructions specific to Planets.
`.codex/config.toml` defaults subagents to Luna low and caps concurrency at four.
No global installation or Cursor configuration is required.

Invoke `$dev-agent-workflow` in Codex. The skill will be available on the next
turn; restart Codex if the native agents are not discovered.

After updating the submodule, compare its `templates/codex/agents/` files with
the installed `.codex/agents/` copies and preserve the local research instructions.
Merge updates explicitly. The installer
does not overwrite existing agents.

Проверяйте фактическую модель при запуске: наличие TOML не доказывает исполнение на Luna.
