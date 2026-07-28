# Big-O

## Quick Revision

- **When to use it:** before choosing an approach, especially from constraints.
- **Core idea:** Big-O describes growth rate as input gets large.
- **Complexity:** common targets are O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!).
- **Template:** estimate work units, then compare to constraints.
- **Common trap:** saying O(n) because there is one loop while ignoring nested work inside it.

## Mental Model

Big-O is not stopwatch time. It is a filter for whether an idea can survive the
largest input. If n is 100, O(n^2) may pass. If n is 100,000, O(n^2) almost never
passes. Use it before coding so you do not polish a doomed brute force.

## How It Works

Count the operation that grows with input. Drop constants and smaller terms:
O(2n + 50) becomes O(n), O(n^2 + n) becomes O(n^2). For recursive code, count
how many calls exist and how much work each call performs.

## Python Template

```python
def estimate(n):
    if n <= 20:
        return "exponential can be acceptable"
    if n <= 5000:
        return "O(n^2) may be acceptable"
    return "aim for O(n log n), O(n), or O(log n)"
```

## Walkthrough

Two Sum brute force checks every pair: about n * n comparisons, so O(n^2).
The hash-map solution scans once and does O(1) average lookup per item, so O(n).

## Edge Cases

- Empty input can make O(1) base handling necessary.
- Very large value range does not imply large input length.
- Sorting changes O(n) ideas into O(n log n).

## Common Mistakes

- Ignoring space complexity.
- Treating Python list membership as O(1); `x in list` is O(n).
- Forgetting that slicing copies lists and strings.

## Practice

- **Anchor problems:** Two Sum, Product of Array Except Self.
- **Extra problems:** Contains Duplicate, Top K Frequent Elements.
- **Interview prompt:** "What complexity does the constraint force?"

## Related Concepts

- `05_python_dsa_toolkit.md`
- `../04_decision_tables.md`
