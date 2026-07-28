# String Algorithms

## Quick Revision

- **When to use it:** substring search, repeated patterns, palindromes, many matches.
- **Core idea:** avoid rechecking characters already proven.
- **Complexity:** KMP O(n + m), rolling hash average O(n).
- **Template:** `kmp_prefix`.
- **Common trap:** relying on rolling hash without collision awareness.

## Mental Model

String algorithms reuse partial match information. If matching fails, they jump
to the longest prefix that could still be valid instead of restarting fully.

## How It Works

KMP builds a prefix table where `pi[i]` is the length of the longest proper prefix
of `pattern[:i+1]` that is also a suffix. During search, mismatch jumps by this
table.

## Python Template

```python
pi = [0] * len(pattern)
j = 0
for i in range(1, len(pattern)):
    while j and pattern[i] != pattern[j]:
        j = pi[j - 1]
```

See `kmp_prefix` in `../03_template_bank.py`.

## Walkthrough

For pattern `ababaca`, the prefix table records that after matching `ababa`, a
mismatch can fall back to length 3 instead of restarting at 0.

## Edge Cases

- Empty pattern.
- Repeated characters.
- Case sensitivity.
- Unicode characters.

## Common Mistakes

- Confusing prefix with substring.
- Wrong fallback index in KMP.
- Treating hash match as guaranteed equality.

## Practice

- **Anchor problems:** Implement strStr, Longest Palindromic Substring.
- **Extra problems:** Repeated Substring Pattern, Palindromic Substrings.
- **Interview prompt:** "What previous character comparisons can be reused?"

## Related Concepts

- `../data-structures/08_tries.md`
- `../techniques/02_sliding_window.md`
