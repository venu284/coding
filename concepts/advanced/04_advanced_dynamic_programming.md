# Advanced Dynamic Programming

## Quick Revision

- **When to use it:** bitmask, interval, tree, digit, multi-dimensional choices.
- **Core idea:** encode every decision dimension in the state.
- **Complexity:** state count times transition cost.
- **Template:** memoized DFS with tuple state.
- **Common trap:** state explosion without pruning.

## Mental Model

Advanced DP is still DP. The difference is that the state has more dimensions or
the fill order is less obvious.

## How It Works

Common advanced states:

- bitmask: which items are used;
- interval: answer for `[left, right]`;
- tree: answer when taking or skipping node;
- digit: position, tight flag, started flag;
- DP on graphs: node plus visited state.

## Python Template

```python
from functools import lru_cache

@lru_cache(None)
def dp(i, mask):
    return best_answer
```

## Walkthrough

Partition to K Equal Sum Subsets can use bitmask DP. The mask says which numbers
are already used, and the current bucket sum determines whether to start the next
bucket.

## Edge Cases

- Duplicate values.
- Large state space.
- Need canonical sorted state.
- Modulo result requirements.

## Common Mistakes

- Missing memoization.
- State includes unnecessary order.
- Not pruning impossible branches early.

## Practice

- **Anchor problems:** Partition to K Equal Sum Subsets, Burst Balloons.
- **Extra problems:** Edit Distance, Traveling Salesman variants.
- **Interview prompt:** "What information must be remembered to avoid recomputation?"

## Related Concepts

- `../algorithms/08_dynamic_programming.md`
- `../techniques/05_backtracking.md`
