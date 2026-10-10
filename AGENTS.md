# Repository Guidelines

## Project Structure & Module Organization

`Planets` currently contains contributor documentation and a project-local Codex workflow. No application source, tests, assets, package manifest, or build configuration exists yet.

The workflow skill is a submodule in `.agents/skills/dev-agent-workflow`; installed Codex agents live in `.codex/agents/`. See `README.md` for cloning and usage instructions.

When implementation begins, group files by responsibility and document the actual layout in `README.md`. Use clear directories such as `src/`, `tests/`, and `assets/` only when the chosen stack needs them. Keep generated output separate from maintained source.

## Build, Test, and Development Commands

No install, development, build, or test commands are configured. Do not assume commands such as `npm test` or `make build` work.

When adding tooling, document exact commands, prerequisites, and required runtime versions in `README.md`. Provide reproducible dependency installation and explain how to run the application locally before requesting review.

## Coding Style & Naming Conventions

No language or formatter has been selected. Follow the chosen language's standard conventions and keep indentation consistent within each file. Use descriptive names that communicate purpose; avoid unexplained abbreviations.

Prefer small, focused modules and existing platform features. If formatting or linting tools are introduced, commit their configuration and document their invocation.

## Testing Guidelines

No test framework or coverage target exists yet. Add tests alongside the first meaningful application behavior, using the selected framework's naming conventions. Cover normal behavior, relevant edge cases, and bug regressions. Document the test command and any required fixtures; keep fixtures free of secrets.

## Commit & Pull Request Guidelines

Use concise, imperative commit subjects such as `Add orbital calculation tests`. No established application commit history exists yet.

Keep changes focused. Pull requests should explain the purpose, summarize changes, list verification performed, and link relevant issues. Include screenshots for visible UI changes and disclose skipped checks.

## Security & Configuration

Never commit credentials, private data, or local environment files. Document required configuration with placeholder values. Keep `.gitignore` updated for generated artifacts and local dependencies; retain shared Codex configuration in version control.
