# Dynamic Programming

## Quick Revision

- **When to use it:** overlapping subproblems with choices, counts, min/max.
- **Core idea:** define state, recurrence, base cases, and fill order.
- **Complexity:** number of states times transition cost.
- **Template:** `house_robber`, `longest_common_subsequence`.
- **Common trap:** coding before defining `dp[i]`.

## Mental Model

DP is remembering answers to smaller decision problems. The hard part is not the
table. The hard part is naming exactly what each state means.

## How It Works

Checklist:

1. State: what does `dp[...]` mean?
2. Choices: what can happen next?
3. Recurrence: how do choices combine?
4. Base cases: smallest valid states.
5. Order: ensure dependencies are ready.

## Python Template

```python
prev2 = prev1 = 0
for value in nums:
    prev2, prev1 = prev1, max(prev1, prev2 + value)
```

See `house_robber` and `longest_common_subsequence` in `../03_template_bank.py`.

## Walkthrough

House Robber state: best money through current house. At each house, either skip
it and keep previous best, or rob it and add to best two houses back.

## Edge Cases

- Empty input.
- One item.
- Base row/column in 2D DP.
- Negative values if allowed.

## Common Mistakes

- Undefined state.
- Off-by-one table dimensions.
- Using updated current-row values when previous-row values are needed.

## Practice

- **Anchor problems:** House Robber, Longest Common Subsequence.
- **Extra problems:** Coin Change, Unique Paths, Word Break.
- **Interview prompt:** "What does one DP cell mean in English?"

## Related Concepts

- `../advanced/04_advanced_dynamic_programming.md`
- `../algorithms/09_greedy.md`
