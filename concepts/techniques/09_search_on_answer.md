# Search On Answer

## Quick Revision

- **When to use it:** minimize maximum, maximize minimum, capacity/rate problems.
- **Core idea:** binary search a value range using a monotonic feasibility check.
- **Complexity:** O(log range * check cost).
- **Template:** `search_on_answer`.
- **Common trap:** feasibility predicate is not monotonic.

## Mental Model

You are not searching an array. You are searching possible answers. If speed `x`
works, then any faster speed also works. That monotonic fact enables binary search.

## How It Works

1. Define answer bounds.
2. Write `can(candidate)`.
3. Prove `can` is monotonic.
4. Binary search for first true or last true.

## Python Template

```python
def can(x):
    return True

ans = search_on_answer(lo, hi, can)
```

See `search_on_answer` in `../03_template_bank.py`.

## Walkthrough

Koko Eating Bananas asks for minimum speed. If speed 6 finishes in time, speed 7
also finishes in time, so the valid region is monotonic.

## Edge Cases

- Lower bound too low.
- Upper bound too low.
- Rounding with ceiling division.
- Impossible cases if problem allows them.

## Common Mistakes

- Searching wrong side after `can(mid)`.
- Off-by-one in answer bounds.
- Predicate too slow.

## Practice

- **Anchor problems:** Koko Eating Bananas, Capacity To Ship Packages.
- **Extra problems:** Split Array Largest Sum, Minimize Maximum Distance.
- **Interview prompt:** "If candidate x works, what about larger or smaller x?"

## Related Concepts

- `../algorithms/02_binary_search.md`
- `../foundations/03_iteration_and_invariants.md`
