# Greedy

## Quick Revision

- **When to use it:** local choice can be proven globally safe.
- **Core idea:** make the best current move and never revisit it.
- **Complexity:** often O(n), or O(n log n) with sorting.
- **Template:** `can_jump`.
- **Common trap:** using greedy without proof.

## Mental Model

Greedy is DP that collapsed because only one running fact matters. If future
choices can invalidate the local choice, use DP instead.

## How It Works

Common greedy proofs:

- exchange argument: swap any optimal solution to include greedy choice;
- stays-ahead: greedy progress is always at least as good;
- invariant: running best preserves all useful history.

## Python Template

```python
farthest = 0
for i, jump in enumerate(nums):
    if i > farthest:
        return False
    farthest = max(farthest, i + jump)
return True
```

See `can_jump` in `../03_template_bank.py`.

## Walkthrough

Jump Game only needs the farthest reachable index. If current index is beyond it,
the path is impossible. Otherwise update reach.

## Edge Cases

- Zero jumps.
- Already at last index.
- Sorting tie rules in interval greedy.
- Negative values if problem allows.

## Common Mistakes

- Choosing local maximum when local feasibility is what matters.
- Not proving correctness.
- Missing sort by end time for interval scheduling.

## Practice

- **Anchor problems:** Jump Game, Gas Station.
- **Extra problems:** Jump Game II, Non-overlapping Intervals.
- **Interview prompt:** "Why will I never regret this local choice?"

## Related Concepts

- `08_dynamic_programming.md`
- `../data-structures/10_intervals.md`
