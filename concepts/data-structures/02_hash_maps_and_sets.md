# Hash Maps And Sets

## Quick Revision

- **When to use it:** find, count, group, duplicate, seen-before.
- **Core idea:** trade space for O(1) average lookup.
- **Complexity:** O(n) time and O(n) space for common one-pass solutions.
- **Template:** `two_sum`, `frequency_map`, `group_by_key`.
- **Common trap:** storing a value before checking can match the same element.

## Mental Model

Hashing answers "have I seen the thing I need?" quickly. It often converts a
nested-loop search into one pass.

## How It Works

Use maps for associations:

- value -> index;
- value -> frequency;
- normalized key -> group;
- prefix sum -> count.

Use sets when the value itself is enough.

## Python Template

```python
seen = {}
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        return [seen[need], i]
    seen[x] = i
```

See `two_sum` in `../03_template_bank.py`.

## Walkthrough

In Two Sum, when you are at `x`, any previous `target - x` completes the answer.
The map makes that lookup constant time on average.

## Edge Cases

- Duplicates.
- Negative numbers.
- Multiple valid answers.
- Empty input.

## Common Mistakes

- Using list membership for O(n) lookup.
- Grouping by a non-normalized key.
- Forgetting hash maps use extra memory.

## Practice

- **Anchor problems:** Two Sum, Group Anagrams.
- **Extra problems:** Valid Anagram, Longest Consecutive Sequence.
- **Interview prompt:** "Can I store what I need later?"

## Related Concepts

- `../techniques/03_prefix_sums.md`
- `../foundations/05_python_dsa_toolkit.md`
