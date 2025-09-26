# (Sub-)Commands

## `git`

go to your terminal and type:

```bash
git
```

You will see a list of git commands and a short description of each command.

## `man`

To get more information about a specific command, you can use the `man` command followed by the command you want to learn more about. For example, to learn more about the `git init` command, you can type:

```bash
man git-init
```

Note the hyphen between `git` and `init`. You can also use the `--help` option or `git help init`.

For example:

```bash
git commit --help
```

## Options

Options are used to modify the behavior of a command. They are usually preceded by a single dash (`-`) for short options or a double dash (`--`) for long options.

For example, the `git commit` command has a `-m` option that allows you to specify a commit message. You can use it like this:
```bash
git commit -m "Initial commit"
```

same with the long option:
```bash
git commit --message "Initial commit"
```

## Questions

- Read the output of `git`, what commands seem the most useful?
- Every commit needs a message. What happens if just do `git commit` without `-m` or `--message`? How can I configure this behavior?

