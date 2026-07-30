# GitHub 101 for AI Builders

A foundation-level, no-code-friendly course for people who create and maintain Markdown files, AI agent instructions, skills, prompts, workflows, and documentation.

## Who this course is for

- Non-technical AI builders
- Vibe coders
- Business owners creating AI agents
- Educators and course creators
- People maintaining `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, prompt libraries, or workflow documentation

## What you will learn

By the end of this course, you will be able to:

1. Explain Git and GitHub in plain English.
2. Create a repository and save Markdown files safely.
3. Understand working directory, staging area, commits, and GitHub.
4. Use essential Git commands.
5. Compare changes and view history.
6. Recover an earlier version of a file.
7. Create branches for safe experiments.
8. Pull and push changes without overwriting teammates' work.
9. Use a simple daily version-control routine for AI projects.

## Course structure

| Module | Topic | Outcome |
|---|---|---|
| 1 | Git, GitHub, and version control | Understand the big picture |
| 2 | Repositories and Markdown | Create your first project |
| 3 | The save workflow | Add, commit, and push |
| 4 | History and comparison | See what changed and why |
| 5 | Restoring earlier work | Recover from mistakes |
| 6 | Branches | Experiment safely |
| 7 | Collaboration | Pull, push, and avoid conflicts |
| 8 | AI-builder workflow | Version AI instructions and skills |

## Start learning

- [Complete Course](COURSE.md)
- [Git Cheat Sheet](resources/git-cheat-sheet.md)
- [Example AI Agent Instructions](examples/AGENTS.md)
- [Final Project](exercises/final-project.md)

## Quick mental model

Think of Git as a time machine on your computer and GitHub as the secure online home for that time machine.

```text
Your file -> git add -> git commit -> git push -> GitHub
             prepare      snapshot      upload
```

## Essential commands

```bash
git status
git add .
git commit -m "Describe the change"
git push
git pull
git log --oneline
git diff
git switch -c experiment-name
```

## Capstone project

Create and version-control an AI agent instruction pack containing:

```text
my-ai-agent/
├── README.md
├── AGENTS.md
├── prompts/
│   ├── research-prompt.md
│   └── writing-prompt.md
└── skills/
    └── customer-support-skill.md
```

Then make three meaningful commits, compare two versions, create an experiment branch, and restore one earlier instruction.

---

Created as a practical foundation course for non-technical people building with AI.