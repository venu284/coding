# DSA Concepts

This folder is the deep-learning companion to `../patterns/`.

- Use `../patterns/` when you want the fastest route to pattern recognition.
- Use `concepts/` when you want to understand every core data structure,
  algorithm, and technique well enough to explain it in an interview.
- Use both together: learn the concept here, then drill the pattern there.

## Read In This Order

| File | What it is | When to use it |
|---|---|---|
| `00_quick_revision_cards.md` | Compact cards for quick interview review | Before timed practice and interviews |
| `01_learning_path.md` | Curriculum-first study order | When learning from scratch or rebuilding fundamentals |
| `02_concept_index.md` | Complete concept lookup table | When you need to jump to one topic |
| `03_template_bank.py` | Runnable Python templates | Type from memory and run to verify |
| `04_decision_tables.md` | Pick the right tool from constraints and triggers | First 2 minutes of a problem |
| `05_practice_map.md` | Anchor and extra problems by concept | Planning practice sessions |
| `06_interview_revision.md` | Last-week, day-before, and same-day review | Interview prep |

## Deep Notes

| Folder | Focus |
|---|---|
| `foundations/` | Big-O, recursion, invariants, math, Python toolkit, testing |
| `data-structures/` | Arrays, maps, stacks, lists, trees, heaps, graphs, tries, union-find, intervals |
| `algorithms/` | Sorting, searching, traversals, graph algorithms, DP, greedy, bits |
| `techniques/` | Two pointers, sliding window, prefix sums, monotonic structures, backtracking |
| `advanced/` | Segment tree, Fenwick tree, advanced graphs, advanced DP, strings, design DSA |

## Daily Workflow

1. Pick a concept from `01_learning_path.md`.
2. Read its quick card in `00_quick_revision_cards.md`.
3. Read the deep-note page for the mental model and traps.
4. Type the related template from `03_template_bank.py` into a blank file.
5. Solve one anchor from `05_practice_map.md`.
6. Log the problem in the repo's normal problem-folder format.

## Interview Workflow

1. Start with `04_decision_tables.md` to identify the likely tool.
2. Review the matching card in `00_quick_revision_cards.md`.
3. Type the template from memory.
4. Solve using the `../patterns/05_interview_mode.md` protocol.
5. Use `06_interview_revision.md` for final-week repetition.

## Verification

Run the template bank:

```bash
python3 concepts/03_template_bank.py
```

Expected:

```text
ALL CONCEPT TEMPLATES PASS
```
