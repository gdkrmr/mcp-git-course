*Lesson 04: Collaboration, Step 02: Forking*

## Forking a Repository

Forking is used when you want to contribute to a repository you don't have write access to (e.g., open source projects).

Forks are a separate copy of the repository with separate permissions, branches, pull requests, and other management tools. **You can make pull requests from your fork to the original repository.**

You usually create a fork if you want to propose changes to a project you don't have write access to.

1. Click "Fork" on the repository page (GitHub, GitLab, etc.). This creates a copy of the repository under your account.
2. Clone your fork to your local machine:
   ```bash
   git clone git@host:user/forked-repo.git
   ```
   You can also simply add it as a separate remote to your clone of the original repository.
3. Create a feature branch, make changes, and push to your fork.
4. Open a pull request from your fork to the original repository.


## Contributing to Open Source

When contributing to open source projects, follow these steps:

1. Read the project's contribution guidelines (often in `CONTRIBUTING.md`).
2. Fork the repository and clone it locally.
3. Create a new branch for your changes.
4. Make your changes and commit them with clear messages.
5. Push your branch to your fork.
6. Open a pull request to the original repository.
7. Participate in code review and respond to feedback.

## Questions

1. Should you fork the Materials Repository? Why or why not?
2. You want to contribute to an open source project on Github. Do you need to fork the repository first? Why or why not?
3. What is the difference between a fork and a branch?
4. You have forked a repository and made changes to its `main` while the original repository has had changes made to its `main`. How do you update your fork's `main` branch with the latest changes from the original repository?
