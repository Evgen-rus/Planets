# Repository Guidelines

## Mission & Scope

Search public TESS observations for uncatalogued transit-like signals. This repository is prepared for a **20–50-star pilot**, not a discovery claim. Read `docs/RESEARCH_PLAN.md`, `docs/NEXT_CHAT.md`, and `config/pilot.toml` before research. Do not expand to 500 stars without user approval.

## Agent Roles

The primary agent manages: define tasks, assign files and budgets, inspect decisive evidence, integrate reports, and accept results. Delegate research, downloads, analysis, implementation, and scientific checks to **GPT-6 Luna**: `worker-low` for routine work, `worker-xhigh` for complex work, `verifier` for independent checking. Preparation in the original setup chat was an explicit exception.

Use project-local `dev-agent-workflow`. Run at most two Luna agents concurrently, with one writer per file and fresh, narrow context. Explicitly select model and effort if custom roles are unavailable. Never silently substitute the primary model. If Luna cannot run, stop and report. Confirm actual execution metadata when available; configuration alone is not proof.

## Project Structure

`scripts/` contains checks; `config/` holds limits; `docs/` contains methodology. `.agents/skills/dev-agent-workflow` is a pinned submodule; `.codex/agents/` holds customized templates. Preserve the submodule and merge template updates explicitly.

Store immutable observations/catalogs in ignored `data/`; derived products, manifests, plots, and checkpoints in ignored `research_outputs/<run_id>/`. Never overwrite completed runs.

## Environment & Testing

Use Python 3.11 in `.venv`. Dependencies are pinned in `requirements.txt`; direct dependencies are in `requirements.in`. Follow `README.md` for installation.

Run `.venv\Scripts\python.exe scripts\check_environment.py` for the offline synthetic BLS check and `git diff --check` before committing. Add targeted scientific tests, including injected transits and noise controls. Synthetic success is not real-data validation.

## Scientific Integrity

Record URLs, UTC retrieval times, SHA-256, units, time conventions, parameters, exclusions, and failures. Count unique TICs actually analyzed. Missing catalogs or unresolved matches block novelty claims. Separate detected signals from vetted candidates. BLS scores are not planet probabilities. Never claim confirmation or NASA follow-up without evidence.

## Style & Contributions

Use four-space Python indentation, `snake_case`, and focused scripts. Use imperative commit subjects. PRs explain purpose, validation, limitations, and issues. No formatter or coverage target is configured. Never commit secrets, environments, raw data, or unreviewed results. Research publication and external submissions require explicit authorization.
