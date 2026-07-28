# Linked Lists

## Quick Revision

- **When to use it:** node references, reverse, merge, cycle, remove nth.
- **Core idea:** change links, not indices.
- **Complexity:** O(n) traversal, O(1) insertion once node is known.
- **Template:** dummy node, prev/curr/next, fast/slow.
- **Common trap:** losing the rest of the list before saving `next`.

## Mental Model

Linked-list problems are pointer choreography. Draw the nodes and make one link
change at a time.

## How It Works

Common moves:

- dummy head removes special cases at the front;
- `prev, curr, next` reverses links;
- fast/slow detects cycles and middle nodes;
- two pointers with a gap remove nth from end.

## Python Template

```python
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
```

See `reverse_list` and `has_cycle` in `../03_template_bank.py`.

## Walkthrough

To reverse a list, save `cur.next`, point `cur.next` backward to `prev`, then move
both pointers forward.

## Edge Cases

- Empty list.
- One node.
- Removing the head.
- Cycle at the head.

## Common Mistakes

- Not using a dummy for deletion.
- Rewiring before saving `next`.
- Forgetting `fast and fast.next`.

## Practice

- **Anchor problems:** Reverse Linked List, Linked List Cycle.
- **Extra problems:** Merge Two Sorted Lists, Remove Nth From End, Reorder List.
- **Interview prompt:** "Which pointers must be saved before rewiring?"

## Related Concepts

- `../techniques/08_fast_slow_pointers.md`
