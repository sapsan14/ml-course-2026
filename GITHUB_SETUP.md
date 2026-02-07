# GitHub repository setup

The project is ready locally. To put it on GitHub:

Russian version: [GITHUB_SETUP_RU.md](GITHUB_SETUP_RU.md)

## 1. Create the repository on GitHub

1. Go to [github.com/new](https://github.com/new).
2. **Repository name:** `ml-course-2026`
3. **Description:** `TalTech Machine Learning for Engineers 2026 — assignments, notebooks, pandas/Colab`
4. Choose **Public** (or Private if you prefer).
5. **Do not** add README, .gitignore, or license (we already have them).
6. Click **Create repository**.

## 2. Push from your machine

In a terminal, from the project folder:

```bash
cd /home/anton/projects/ml-course-2026
git init
git add .
git commit -m "Initial: EX01 assignment, README, workflow, project plan"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ml-course-2026.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

If you use SSH:

```bash
git remote add origin git@github.com:YOUR_USERNAME/ml-course-2026.git
git push -u origin main
```

## 3. Optional: add Cursor rule for this repo

To give the AI context about the course and EX01, you can add a rule file:

- Create `.cursor/rules/ml-course.mdc` with a short note that this is the TalTech ML 2026 repo, EX01 is Pandas cleaning, variable names must match the assignment, and to use ASSIGNMENT_EX01.md for steps and prompts.

After that you can clone or open the repo from GitHub in Cursor on any machine.
