# Bit Manipulation

## Quick Revision

- **When to use it:** XOR, masks, count bits, no extra space, powers of two.
- **Core idea:** operate on binary representation directly.
- **Complexity:** O(n) for array folds, O(number of bits) for bit loops.
- **Template:** `single_number`, `count_bits`.
- **Common trap:** forgetting `n & (n - 1)` clears the lowest set bit.

## Mental Model

Bits are compact booleans. XOR is especially useful because equal values cancel:
`x ^ x = 0` and `x ^ 0 = x`.

## How It Works

Useful operations:

- `x & 1`: odd/even bit.
- `x >> 1`: divide by 2 ignoring remainder.
- `x << 1`: multiply by 2.
- `x & (x - 1)`: remove lowest set bit.
- `x ^ y`: toggle differences.

## Python Template

```python
ans = 0
for num in nums:
    ans ^= num
return ans
```

See `single_number` and `count_bits` in `../03_template_bank.py`.

## Walkthrough

Single Number XORs all values. Paired duplicates cancel to zero, leaving the one
unpaired value.

## Edge Cases

- Zero.
- Negative numbers in Python use unbounded signed integers.
- Fixed 32-bit output problems.
- Overflow assumptions from other languages do not apply.

## Common Mistakes

- Using addition where XOR cancellation is needed.
- Forgetting masks for 32-bit simulations.
- Misreading bit positions as 1-indexed.

## Practice

- **Anchor problems:** Single Number, Number of 1 Bits.
- **Extra problems:** Counting Bits, Reverse Bits, Sum of Two Integers.
- **Interview prompt:** "Which bit identity removes the duplicate work?"

## Related Concepts

- `../foundations/04_math_for_dsa.md`
- `../advanced/04_advanced_dynamic_programming.md`
