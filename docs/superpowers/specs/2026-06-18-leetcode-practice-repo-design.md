# LeetCode Practice Repo Design

## Goal

Create a lightweight Python-focused repository for daily LeetCode practice. Each solved problem gets its own folder named after the problem title, and each folder contains the submitted solution plus a README for learning notes and reflection.

## Repository Layout

The repository will use this structure:

```text
.
├── README.md
├── templates/
│   └── problem-readme.md
└── two-sum/
    ├── README.md
    └── solution.py
```

`two-sum/` is an example starter problem folder. Future folders should use normalized problem titles, such as `valid-parentheses/` or `best-time-to-buy-and-sell-stock/`.

## Files

### Global README

`README.md` will explain the purpose of the repository, the daily workflow, the naming convention, and the expected folder structure for each problem.

### Problem README Template

`templates/problem-readme.md` will be the reusable template for each problem's notes. It will include sections for:

- Problem link
- Difficulty
- Topics
- Approach
- Complexity
- Key learnings
- Mistakes or edge cases
- Reflection
- Follow-up ideas

### Starter Problem Folder

`two-sum/` will provide a concrete example of the intended structure:

- `two-sum/README.md` copied from the problem README template
- `two-sum/solution.py` with a minimal Python solution skeleton

## Python Scope

The repo will stay Python-focused but lightweight. It will not add packaging, dependency management, or test tooling yet. That keeps daily entries fast to create and avoids extra ceremony for short LeetCode solutions.

## Error Handling And Maintenance

The main maintenance concern is consistent naming. Problem folders should be lowercase kebab-case derived from the LeetCode title. If two problems ever normalize to the same folder name, append a short disambiguator.

## Testing And Verification

Verification for the initial scaffold is file-based:

- Confirm the expected files exist.
- Confirm the README template has reflection and learning sections.
- Confirm the Python solution file is syntactically valid.
