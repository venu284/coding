# Math For DSA

## Quick Revision

- **When to use it:** modulo, gcd, parity, coordinate geometry, counting, powers.
- **Core idea:** arithmetic properties can remove loops or reduce state.
- **Complexity:** gcd and fast power are O(log n).
- **Template:** gcd, modulo count, parity, integer bounds.
- **Common trap:** negative division and modulo behavior.

## Mental Model

Most interview math is not advanced math. It is pattern recognition: parity,
divisibility, prefix differences, combinations, and safe integer reasoning.

## How It Works

Useful identities:

- XOR cancels equal values.
- Sum 1..n is `n * (n + 1) // 2`.
- `gcd(a, b) == gcd(b, a % b)`.
- `(a + b) % m == ((a % m) + (b % m)) % m`.

## Python Template

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
```

## Walkthrough

Missing Number can be solved by expected sum minus actual sum. It can also be
solved by XOR because every duplicate index/value pair cancels out.

## Edge Cases

- Zero values.
- Negative values.
- Large products before modulo.
- Integer division with negatives.

## Common Mistakes

- Using `/` instead of `//`.
- Forgetting parentheses in modulo expressions.
- Assuming floating-point equality is exact.

## Practice

- **Anchor problems:** Missing Number, Pow(x, n).
- **Extra problems:** Happy Number, Plus One, Sqrt(x).
- **Interview prompt:** "Can arithmetic replace the loop or the extra memory?"

## Related Concepts

- `../algorithms/10_bit_manipulation.md`
- `../techniques/03_prefix_sums.md`
