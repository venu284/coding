# Monotonic Stack And Queue

## Quick Revision

- **When to use it:** next greater/smaller, histogram, sliding window maximum.
- **Core idea:** keep candidates in useful sorted order.
- **Complexity:** O(n); each index is pushed and popped at most once.
- **Template:** `daily_temperatures`, `sliding_window_max`.
- **Common trap:** storing values when indices are needed.

## Mental Model

A monotonic structure throws away candidates that can never win in the future.
That is why it stays linear.

## How It Works

Monotonic stack:

- while current resolves stack top, pop and answer;
- push current index.

Monotonic queue:

- remove expired indices from front;
- remove weaker candidates from back;
- front is best candidate.

## Python Template

```python
while stack and nums[stack[-1]] < nums[i]:
    j = stack.pop()
    ans[j] = i - j
stack.append(i)
```

See `daily_temperatures` in `../03_template_bank.py`.

## Walkthrough

Daily Temperatures stores days waiting for a warmer day. When a warmer
temperature arrives, it resolves all cooler days at the stack top.

## Edge Cases

- Equal values.
- No greater value.
- Window expiration.
- Need distance vs value.

## Common Mistakes

- Wrong increasing/decreasing direction.
- Popping equal values incorrectly.
- Forgetting to remove expired queue indices.

## Practice

- **Anchor problems:** Daily Temperatures, Sliding Window Maximum.
- **Extra problems:** Largest Rectangle in Histogram, Next Greater Element.
- **Interview prompt:** "Which candidates are now impossible?"

## Related Concepts

- `../data-structures/03_stacks_and_queues.md`
