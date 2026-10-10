# Planets

Project workspace. Application code and development tooling have not been added yet.

See [AGENTS.md](AGENTS.md) for contributor guidelines.

## Clone

```sh
git clone --recurse-submodules https://github.com/Evgen-rus/Planets.git
```

For an existing checkout, run `git submodule update --init --recursive`.

## Project-local Codex workflow

The `dev-agent-workflow` skill is pinned as a submodule at
`.agents/skills/dev-agent-workflow`. Its four Codex agent templates are tracked
in `.codex/agents/`. No global installation or Cursor configuration is required.

Invoke `$dev-agent-workflow` in Codex. The skill will be available on the next
turn; restart Codex if the native agents are not discovered.

After updating the submodule, compare its `templates/codex/agents/` files with
the installed `.codex/agents/` copies and merge updates explicitly. The installer
does not overwrite existing agents.
