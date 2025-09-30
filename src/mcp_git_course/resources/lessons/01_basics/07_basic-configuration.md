*Lesson 01: Basics, Step 07: Basic Configuration*
# Basic Configuration

## Configure username and email

To function properly, git needs to know your name and email.

1. Configure your username:
   ```bash
   git config --global user.name "Your Name"
   ```

2. Configure your email:
   ```bash
   git config --global user.email "you@example.com"
   ```

## Verify Configuration

To check your configuration settings, run:
```bash
git config --global --list
```
You should see an output listing your configured username and email:
```
user.name=Your Name
user.email=you@example.com
```

## Questions
1. `git config user.name "Your Name"` only acts on the local repository. Why this is useful.
2. Look at the output of `man git-config`. What does `init.defaultBranch` do?
3. Set `init.defaultBranch` to `main`. How does your global config look like?
