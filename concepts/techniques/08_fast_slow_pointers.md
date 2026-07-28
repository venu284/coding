# Fast Slow Pointers

## Quick Revision

- **When to use it:** linked-list cycle, middle, kth from end, repeated-state cycles.
- **Core idea:** pointers moving at different speeds reveal structure.
- **Complexity:** O(n) time, O(1) space.
- **Template:** `has_cycle`.
- **Common trap:** not checking `fast and fast.next`.

## Mental Model

If a fast pointer laps a slow pointer, a cycle exists. If fast reaches the end,
slow is near the middle.

## How It Works

Move slow one step and fast two steps. For cycle detection, equality means they
met inside a loop. For middle, when fast stops, slow marks the middle.

## Python Template

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

See `has_cycle` in `../03_template_bank.py`.

## Walkthrough

In Linked List Cycle, if there is no cycle, fast reaches `None`. If there is a
cycle, fast eventually catches slow.

## Edge Cases

- Empty list.
- One node with no cycle.
- One node pointing to itself.
- Even vs odd length middle.

## Common Mistakes

- Accessing `fast.next.next` without checking.
- Comparing node values instead of node identity.
- Using extra set when O(1) space is required.

## Practice

- **Anchor problems:** Linked List Cycle, Middle of Linked List.
- **Extra problems:** Happy Number, Find Duplicate Number.
- **Interview prompt:** "Can two speeds reveal the hidden structure?"

## Related Concepts

- `../data-structures/04_linked_lists.md`
