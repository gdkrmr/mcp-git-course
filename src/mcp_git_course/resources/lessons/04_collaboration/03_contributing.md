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
- Keep your branches up to date with the main branch (`git pull origin main`).
- Communicate with your team and respond to code review feedback.
