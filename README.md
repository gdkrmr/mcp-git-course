# Learn `git` with LLMs

Use your local LLM client to learn `git` interactively with the help of this course.

## How it works

This repository contains an MCP server that instructs your LLM client teach you `git`. It contains course materials and instructions.

It also keeps track of your progress, so you can continue where you left off.

To use, add the mcp server to your local LLM client and say `start git course` to begin the course. You can restart the course at any time by saying `restart git course`.

## How to use

### Requirements

A local LLM client that supports MCP servers, such as [Zed](https://zed.dev), [Claude code](https://claude.ai), [VS Code](https://code.visualstudio.com), or [Gemini](https://ai.google.dev/gemini).

### Installation

install via [`pipx`](https://pipx.pypa.io/latest/installation):

```bash
pipx install git+https://github.com/gdkrmr/git-mcp-course.git
```

This will install the `mcp-git-course` command, which is the MCP server that serves the course materials.

update the package:

```bash
pipx upgrade git+https://github.com/gdkrmr/git-mcp.git
```

### Configure for your client
#### Zed
Add the following to `~/.config/zed/settings.json`
```json
{
  ...,
  "context_servers": {
    "git_course": {
      "source": "custom",
      "enabled": true,
      "command": "mcp-git-course",
      "args": [],
      "env": {}
    },
    ...
  },
  ...
}
```

#### Claude code
TODO
#### VS Code
TODO
#### Gemini
TODO

## Manually following the course

You can also access the course materials [here](https://github.com/gdkrmr/git-mcp/tree/master/src/mcp_git/resources/lessons) without having an LLM as an intermediary.

## Notice

This work was inspired by the [mastra mcp server](https://github.com/mastra-ai)
