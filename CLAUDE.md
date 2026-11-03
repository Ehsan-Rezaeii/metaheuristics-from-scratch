# CLAUDE.md — Instructions for Claude Code

This repository is part of a 6-project GitHub portfolio called
"AI for Software Engineering", built by Ehsan Rezaei (GitHub: Ehsan-Rezaeii),
an undergraduate student who is a complete beginner in Python, machine learning,
Git, and research. The portfolio is for a research collaboration with
Dr. Bahman Arasteh (Software Engineering, Istinye University), whose work is on
search-based software engineering, AI-based software testing, software security,
metaheuristic optimization, and machine learning.

The student must be able to explain and defend every line of this project.
Learning matters more than speed.

## How to work with me

- Do ONE small step per request, then stop and wait. Never build the whole
  project at once.
- Do not add anything outside the plan unless I ask. Keep things lightweight
  (each project is about 3-4 hours of work and must run on a normal laptop).
- If a step gets too complex or slow, propose a simpler option instead.
- If my instruction is wrong or there is a better way, say so clearly.

## Language rules

- Code, variable names, comments, docstrings, README, and commit messages:
  simple English.
- Your explanations to me in chat: Persian (Farsi).
- In Persian text, write every English term, tool, library, or command in
  English, and right after it give a one-line Persian explanation in
  parentheses. Do this every time, even if you explained it before.
- Persian text must render right-to-left: every paragraph, line, heading, and
  list item must start with a Persian word (put a Persian word before any
  English term, number, or link at the start of a line). Code blocks are exempt.

## After each step, explain in Persian

1. What you changed (which files) and why, section by section.
2. Which parts of the diff I should read carefully.
3. How to check that it works (the exact command and what output to expect).
4. Any new concept, explained with a simple everyday example.

When you show results, explain what the numbers mean and whether they are good
or bad. Never invent, guess, or round up results. Only report numbers you
actually got from running the code.

When there is an error: first explain in one simple sentence what it means,
then the fix, then why it happened.

## Repository structure (keep this exact layout)

```
project-name/
├── README.md
├── CLAUDE.md
├── requirements.txt
├── LICENSE
├── .gitignore          # data/, .venv/, __pycache__/, .ipynb_checkpoints/, .env
├── data/               # raw data (NOT committed) + download instructions
├── src/                # main Python code (functions, algorithms)
├── notebooks/          # experiments and plots that call src/
├── results/            # tables (CSV/Markdown) and figures (PNG) used in README
└── tests/              # pytest unit tests
```

## Code standards

- Small functions with a short docstring and simple type hints.
- No absolute paths (like C:\Users\...). Use paths relative to the repo root.
- Put settings (seed, number of runs, budgets) as constants at the top of files.
- Always use a fixed random seed for reproducibility.
- Main logic lives in src/. Notebooks only call src/ functions and must run top
  to bottom without errors, with outputs saved.
- Pin library versions in requirements.txt.
- Write pytest tests for important logic and run them before committing.

## Git rules

- Small, real commits with short meaningful messages,
  e.g. "Add binary GWO feature selection". One commit per logical step.
- Never commit data files, large files, .venv/, or secrets.
- Never commit API keys or passwords. Use environment variables or a .env file
  (which is in .gitignore).
- Never rewrite history or change commit dates.

## Data and honesty

- Data goes in data/ and is not committed. The README must give the dataset
  link, license, and exact download steps.
- Avoid data leakage: scaling, SMOTE, and feature selection are fit only on
  training data (inside cross-validation where needed).
- When a result depends on a paper, give the real title and DOI only after
  verifying it. Never make up references.
- Credit any borrowed code in the README References section.

## Environment notes

- The cloud session's network may block dataset sites (Kaggle, UCI, OpenML).
  If a download fails, tell me and suggest options; do not work around blocks.
- No GPU in the cloud session. Deep learning and LLM steps run in Google Colab
  or Kaggle Notebooks; prepare notebooks for that.
- The student's laptop: Windows, Python 3.14, VS Code, 16 GB RAM,
  GTX 1050 Ti (4 GB).

## This project

Project 1 of 6: `metaheuristics-from-scratch`

Goal: implement four classic metaheuristic optimizers from scratch with NumPy,
compare them on standard benchmark functions, and build binary versions for
feature selection. Later projects (2, 4, 6) reuse the binary versions, so the
code must be a clean, reusable library.

Algorithms: GA (Genetic Algorithm), PSO (Particle Swarm Optimization),
GWO (Grey Wolf Optimizer), WOA (Whale Optimization Algorithm).

Data: no external dataset. Benchmark functions are written in code. The small
feature-selection test uses scikit-learn's built-in breast cancer dataset
(`sklearn.datasets.load_breast_cancer`), so no download is needed.

Design rules for this project:
- All optimizers share one interface, e.g.
  `optimize(objective, dim, bounds, pop_size, max_iter, seed)` returning the
  best solution, the best value, and the convergence curve (best value per
  iteration).
- Solutions must always stay inside the bounds.
- Same seed must give exactly the same result.
- Minimization is the default.

Steps (one per session request; write tests together with each step):
1. Repo setup: folder structure, requirements.txt, empty package in src/.
2. Benchmark functions: Sphere, Rastrigin, Ackley, Rosenbrock (dim = 30),
   with tests that check the known optimum value.
3. GA, PSO, GWO, WOA with the shared interface, with tests (stays in bounds,
   gets close to 0 on Sphere, reproducible with a fixed seed).
4. Binary versions with S-shaped and V-shaped transfer functions, with tests.
5. Main experiment: 30 independent runs per algorithm per function; table of
   mean, std, and best in results/; convergence plots; Wilcoxon rank-sum test
   (scipy). Keep run time reasonable on a laptop.
6. Small feature-selection experiment on the breast cancer dataset with the
   binary versions (fitness = classifier error from cross-validation on
   training data + small penalty for the number of selected features).
7. GitHub Actions workflow that runs pytest on every push; add the CI badge.
8. README with real results, following the template in the project plan.
