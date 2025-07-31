# Learn `git` with LLMs

Use your local LLM client to learn `git` interactively with the help of this course.

## How it works

This repository contains an MCP server that instructs your LLM client teach you `git`. It contains course materials and instructions.

It also keeps track of your progress, so you can continue where you left off.

## Requirements

A local LLM client that supports MCP servers, such as [Zed](https://zed.dev), [Claude code](https://claude.ai), [VS Code](https://code.visualstudio.com), or [Gemini](https://ai.google.dev/gemini).

## How to use

## Run from anywhere
```bash
uvx --from git+https://github.com/gdkrmr/rdm-mcp main.py
```

## Configure for your client
### Zed
Add the following to `~/.config/zed/settings.json`
```json
{
  ...,
  "context_servers": {
    "git_course": {
      "source": "custom",
      "enabled": true,
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/gdkrmr/git-mcp",
        "main.py"
      ],
      "env": {}
    },
    ...
  },
  ...
}
```

### Claude code
TODO
### VS Code
TODO
### Gemini
TODO

# Manually following the course

You can access the course materials [here](./resources/lessons/overview.md).

# Notice

This work was inspired by the [mastra mcp server](https://github.com/mastra-ai)
