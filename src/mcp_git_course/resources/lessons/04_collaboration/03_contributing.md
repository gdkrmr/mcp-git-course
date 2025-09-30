*Lesson 04: Collaboration, Step 03: Contributing*

## Feature Branch Workflow

A feature branch workflow allows each contributor to work on their own branch, separate from the main codebase.

1. **Create a new branch for your feature or fix:**
   ```bash
   git checkout -b feature/my-new-feature
   ```
2. **Work on your changes and commit them:**
   ```bash
   git add .
   git commit -m "Add my new feature"
   ```
3. **Push your branch to the remote repository:**
   ```bash
   git push origin feature/my-new-feature
   ```
4. **Open a pull request (see next step) to merge your branch into the main branch.**

## Best Practices

- Always work on a separate branch for each feature or fix.
- Write clear, descriptive commit and pull request messages.
- Keep your branches up to date with the main branch:
  ```bash
  git fetch origin
  git rebase origin/main
  ```
  or
  ```bash
  git merge origin/main
  ```
- Communicate with your team and respond to code review feedback.
- Keep changes small and focused to simplify reviews.
- Add tests or documentation updates as part of the same feature branch when applicable.

## Suggested Pull Request Template (example)

Title: [feature] Short summary of the change

Description:
- What does this change do?
- Why is this necessary?
- How to test / steps to verify
- Screenshots or logs (if applicable)
- Related issues / tickets

## Typical Contribution Flow

1. Fork or clone the repository (if you don't have write access, fork first).
2. Create a branch for your work.
3. Implement the change with appropriate tests.
4. Run the test suite and linters locally.
5. Push the branch and open a pull/merge request.
6. Address review comments, update the branch, and re-run tests.
7. Once approved, merge according to the project's merge strategy (squash, rebase, merge commit).

## Handling Feedback and Iteration

- Respond to comments politely and make requested changes in the same branch.
- If feedback requires a large refactor, consider splitting into follow-up PRs.
- Use comments to explain reasoning for design decisions when reviewers ask questions.

## Questions

1. Should you fork the Materials Repository? Why or why not?
2. You want to contribute to an open source project on GitHub. Do you need to fork the repository first? Why or why not?
3. What is the difference between a fork and a branch?
4. You have forked a repository and made changes to its `main` while the original repository has had changes made to its `main`. How do you update your fork's `main` branch with the latest changes from the original repository?
