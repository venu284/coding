# Python DSA Toolkit

## Quick Revision

- **When to use it:** every Python interview solution.
- **Core idea:** standard library choices often decide complexity.
- **Complexity:** know each container's real operation costs.
- **Template:** `Counter`, `defaultdict`, `deque`, `heapq`, `bisect`.
- **Common trap:** using a list as a queue with `pop(0)`.

## Mental Model

Python gives you strong building blocks, but each has a cost model. The goal is
not to memorize every method. The goal is to know which operation stays fast.

## How It Works

Core imports:

```python
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from functools import lru_cache
from math import inf
```

## Python Template

```python
counts = Counter(nums)
q = deque([start])
heap = []
heappush(heap, (priority, item))
```

See `../03_template_bank.py` for runnable examples.

## Walkthrough

Top K Frequent uses `Counter` for frequencies and `heapq` for a size-k heap. That
turns sorting all unique values into keeping only the k best candidates.

## Edge Cases

- `defaultdict(list)` creates entries when read.
- Heap tuples compare later fields if priorities tie.
- `set` and `dict` are average O(1), not worst-case O(1).

## Common Mistakes

- `list.pop(0)` in BFS.
- Sorting when a heap or counter is simpler.
- Mutating a collection while iterating over it.

## Practice

- **Anchor problems:** Top K Frequent Elements, Group Anagrams.
- **Extra problems:** Kth Largest Element, Find Median from Data Stream.
- **Interview prompt:** "Which Python container gives the operation you need?"

## Related Concepts

- `../data-structures/02_hash_maps_and_sets.md`
- `../data-structures/06_heaps_priority_queues.md`
- `../data-structures/03_stacks_and_queues.md`
