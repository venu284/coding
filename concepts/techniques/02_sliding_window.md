# Sliding Window

## Quick Revision

- **When to use it:** contiguous subarray or substring with a condition.
- **Core idea:** expand right, shrink left when invalid.
- **Complexity:** O(n) because each index enters and leaves once.
- **Template:** `longest_unique_substring`.
- **Common trap:** wrong shrink condition.

## Mental Model

The window is the current candidate range. You only move forward; no index needs
to be reconsidered after it leaves the window.

## How It Works

For variable windows:

1. Add `right`.
2. Update state.
3. While invalid, remove `left`.
4. Update best answer.

## Python Template

```python
left = 0
for right, ch in enumerate(s):
    while invalid:
        left += 1
```

See `longest_unique_substring` in `../03_template_bank.py`.

## Walkthrough

Longest Substring Without Repeating Characters moves `left` past the previous
copy of a repeated character. The current window remains unique.

## Edge Cases

- Empty string.
- All same characters.
- All unique characters.
- Condition uses "at most" vs "exactly".

## Common Mistakes

- Shrinking only once when multiple removals are needed.
- Updating answer before restoring validity.
- Confusing fixed-size and variable-size windows.

## Practice

- **Anchor problems:** Longest Substring Without Repeating Characters, Best Time to Buy/Sell Stock.
- **Extra problems:** Character Replacement, Minimum Window Substring.
- **Interview prompt:** "What makes the window invalid?"

## Related Concepts

- `../data-structures/02_hash_maps_and_sets.md`
- `03_prefix_sums.md`
