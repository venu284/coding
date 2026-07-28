# Testing Edge Cases

## Quick Revision

- **When to use it:** before submitting every solution.
- **Core idea:** test categories, not just samples.
- **Complexity:** small upfront cost, large correctness payoff.
- **Template:** happy path -> edge -> boundary -> tricky.
- **Common trap:** only testing the given example.

## Mental Model

Hidden tests usually check shape, not mystery. They target empty input, minimum
input, duplicates, negatives, sorted/reverse sorted order, and values at limits.

## How It Works

Build a small test set:

1. Sample or happy path.
2. Empty or minimum input.
3. Duplicates or repeated state.
4. Boundary values from constraints.
5. A case that breaks your first idea.

## Python Template

```python
assert solution(sample) == expected
assert solution(edge_case) == expected
assert solution(boundary_case) == expected
assert solution(tricky_case) == expected
```

## Walkthrough

For Valid Anagram, test same letters, different lengths, repeated letters, and
empty strings. Different lengths should fail before doing extra work.

## Edge Cases

- Empty list/string.
- One item.
- All values identical.
- Negative numbers.
- Duplicates.
- Already sorted and reverse sorted.

## Common Mistakes

- Forgetting impossible inputs from constraints.
- Not testing duplicates.
- Not testing the smallest valid input.

## Practice

- **Anchor problems:** Valid Anagram, Valid Palindrome.
- **Extra problems:** Two Sum, Merge Intervals, Binary Search.
- **Interview prompt:** "Which hidden test would break this?"

## Related Concepts

- `01_big_o.md`
- `05_python_dsa_toolkit.md`
