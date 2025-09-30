# Learn `git` with LLMs

Use your local LLM client to learn `git` interactively with the help of this course.

## How it works

- This repository contains an MCP server that instructs your LLM client teach you `git`. It contains course materials and instructions.
- It also keeps track of your progress, so you can continue where you left off.
- To use, add the MCP server to your local LLM client and say `start git course` to begin the course. You can restart the course at any time by saying `restart git course`.
- The MCP server keeps track of your progress, you can ask it to `resume the git course` and it will resume the course.

## How to use

- Set up your local LLM client.
- Install and add `mcp-git-course` as an MCP server to your client.
- Ask your LLM client to "start the git course".

## Requirements

A local LLM client that supports MCP servers, such as [Zed](https://zed.dev), [Claude code](https://claude.ai), [VS Code](https://code.visualstudio.com), or [Gemini](https://ai.google.dev/gemini).

### Installation

#### `pipx`

install via [`pipx`](https://pipx.pypa.io/latest/installation):

```bash
pipx install git+https://github.com/gdkrmr/git-mcp-course.git
```

This will install the `mcp-git-course` command, which is the MCP server that serves the course materials.

update the package:

```bash
pipx upgrade git+https://github.com/gdkrmr/git-mcp-course.git
```

#### `uvx`

use directly via [`uvx`](https://docs.astral.sh/uv/), `uvx` takes care of installation on the fly. Configure as 

```json
{
  "git_course": {
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/gdkrmr/mcp-git-course@master",
      "mcp-git-course"
    ]
  }
}
```

note that the exact configuration may be slightly different

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

#### gemini-cli

Add this to your `~/.gemini/settings.json` file:

```json
{
  "mcpServers": {
    "serverName": {
      "command": "mcp-git-course",
      "args": [],
      "env": {},
      "cwd": "",
      "timeout": 30000,
      "trust": false
    }
  }
}
```

## Manually following the course

You can also access the course materials [here](https://github.com/gdkrmr/mcp-git-course/tree/master/src/mcp_git_course/resources/lessons) without having an LLM as an intermediary.

## Notice

This work was inspired by the [mastra mcp server](https://github.com/mastra-ai).

