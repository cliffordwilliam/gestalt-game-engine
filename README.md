# gestalt-game-engine

My in-house game engine

## The following are steps to set this up in your local machine and start working on it

Read the following to run this project in your local machine

### This thing uses python 3.13, make sure to install that before hand

The steps to do that is online, just go look it up yourself

### This project was worked on using VS Code

Get the following extensions all from Microsoft

- Pylance
- Python
- Python Debugger

### Uv setup

Everything written here is from [uv official doc](https://docs.astral.sh/uv)

So things may or may not have changed at the time of reading this

This is for windows, first you want to install uv in your machine in powershell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then you want to use it to npm init

```powershell
uv init
```

The above will create the following

```
.
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

The python version holds the python version you use, uv needs this to make venv

You can use uv to run the main.py

```bash
uv run main.py
```

After running it for the first time, uv will create venv and lock and toml

- lock acts like package.lock.json
    - cross platform dep list, commit this to ensure consistent install in any os
- toml acts like package.json
    - project metadata and also deps

Use uv to install dep, like npm i, dep are all dumped into venv

Whenever you do `uv run`, that uses the venv

This is how you manage dep with uv

Just like npm i

```powershell
uv add requests
```

Just like npm un

```powershell
uv remove requests
```

Upgrade dep

```powershell
uv lock --upgrade-package requests
```

### Ruff for linter and formater

Everything written here is from [ruff official doc](https://docs.astral.sh/ruff/)

So things may or may not have changed at the time of reading this

I am not going to add ruff as dep, because I am using vs code and it has ruff extension

Get vs code ruff extension version 2024.32.0 or later

At the time i am using 2025.14.0

The rest of what is written here is from the ruff vs code extension doc

As in just click the ruff extension from vs code extension listing

Taken together, you can configure Ruff to format, fix, and organize imports on-save

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

Ruff comes with language server that is automatically on

### Ruff pre commit

Everything written here is from [ruff official doc](https://docs.astral.sh/ruff/)

This is a pre-commit hook for ruff

get the pre commit dep, this is not in doc but we need it

```powershell
uv add pre-commit
```

Add this to add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.9.9
  hooks:
    # Run the linter.
    - id: ruff
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
```

Tell pre commit to install that yaml so it knows what to do on commit

```powershell
uv run pre-commit install
```

Now on every commit that ruff and lint will run, if it fails commit fails
