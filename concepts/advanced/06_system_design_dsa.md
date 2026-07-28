# System Design DSA

## Quick Revision

- **When to use it:** design cache, leaderboard, rate limiter, autocomplete.
- **Core idea:** combine data structures to meet operation constraints.
- **Complexity:** state each operation separately.
- **Template:** `LRUCache`.
- **Common trap:** making one operation fast while another becomes too slow.

## Mental Model

Design-style DSA is about APIs and operation budgets. Start from required methods,
then choose structures that maintain the needed invariants.

## How It Works

Examples:

- LRU Cache: hash map for lookup plus doubly linked list for recency.
- Min Stack: normal stack plus min stack.
- Leaderboard: map for scores plus sorted structure or heap depending on queries.
- Autocomplete: trie plus ranking metadata.

## Python Template

```python
cache = LRUCache(2)
cache.put(1, 1)
value = cache.get(1)
```

See `LRUCache` in `../03_template_bank.py`.

## Walkthrough

LRU Cache needs O(1) get and put. The hash map finds nodes; the linked list moves
recently used nodes to the end and evicts from the front.

## Edge Cases

- Capacity 1.
- Updating existing key.
- Getting missing key.
- Evicting after insert.

## Common Mistakes

- Forgetting to move key on get.
- Leaving stale nodes in list or heap.
- Not defining method complexity.

## Practice

- **Anchor problems:** LRU Cache, Min Stack.
- **Extra problems:** LFU Cache, Design Twitter, Time Based Key-Value Store.
- **Interview prompt:** "What does each operation need to cost?"

## Related Concepts

- `../data-structures/04_linked_lists.md`
- `../data-structures/02_hash_maps_and_sets.md`
- `../data-structures/08_tries.md`
