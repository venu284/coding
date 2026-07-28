# Backtracking

## Quick Revision

- **When to use it:** all subsets, permutations, combinations, partitions, boards.
- **Core idea:** choose, explore, unchoose.
- **Complexity:** exponential; expected for all-solutions problems.
- **Template:** `subsets`.
- **Common trap:** appending the live path instead of a copy.

## Mental Model

Backtracking walks a decision tree. Each recursive call represents a partial
choice. Undoing the choice restores the state for the next branch.

## How It Works

1. If the partial solution is complete, record it.
2. Iterate possible choices.
3. Apply a choice.
4. Recurse.
5. Undo the choice.

## Python Template

```python
path.append(choice)
backtrack(next_state)
path.pop()
```

See `subsets` in `../03_template_bank.py`.

## Walkthrough

Subsets has a binary decision for each number: skip it or take it. After n
decisions, record the path.

## Edge Cases

- Empty input.
- Duplicate candidates.
- Need sorted output or unique combinations.
- Board boundary checks.

## Common Mistakes

- Not copying `path`.
- Forgetting to pop.
- No pruning when constraints allow it.

## Practice

- **Anchor problems:** Subsets, Combination Sum.
- **Extra problems:** Permutations, Word Search, Palindrome Partitioning.
- **Interview prompt:** "What are the choices at each level?"

## Related Concepts

- `../foundations/02_recursion.md`
- `../data-structures/08_tries.md`
