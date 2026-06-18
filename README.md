# LeetCode Practice

Daily LeetCode practice repository for Python solutions, notes, and reflections.

Each problem has its own folder named after the problem title using lowercase kebab-case.

## Layout

```text
.
├── README.md
├── templates/
│   └── problem-readme.md
└── problem-title/
    ├── README.md
    └── solution.py
```

## Daily Workflow

1. Solve a LeetCode problem.
2. Create a folder using the problem title, such as `two-sum`.
3. Add the accepted Python solution in `solution.py`.
4. Copy `templates/problem-readme.md` into the problem folder as `README.md`.
5. Record the approach, mistakes, edge cases, learnings, and reflections.

## Naming Convention

Use lowercase kebab-case based on the LeetCode title:

- `Two Sum` -> `two-sum`
- `Valid Parentheses` -> `valid-parentheses`
- `Best Time to Buy and Sell Stock` -> `best-time-to-buy-and-sell-stock`

If two titles normalize to the same folder name, append a short disambiguator.

## Problem Folder Checklist

- `README.md` contains notes, learnings, and reflections.
- `solution.py` contains the Python solution submitted or practiced.
- Complexity analysis is recorded after solving.
- Any mistakes or edge cases are written down while still fresh.
