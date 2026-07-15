# Pattern Speedrun — the fast track to interview-ready

**This folder is the primary, fast-pace study system.** It replaces problem-grinding
with pattern-mastery: learn the 19 shapes behind Blind 75, install their templates
cold, then let repetition make recognition automatic.

> The old week-by-week doc (`../DSA_Plan.md`) is the **long track** — a 26-week,
> concept-first walk through the full Blind 75 → NeetCode 150. Use it as a reference
> for extra problems and deeper concept notes. This folder is the single source of
> truth for the fast path; where the two differ, follow this folder.

## The theory (why this is faster)
75 problems ≈ **19 patterns wearing costumes**. Grinding problems relearns the same
pattern 4 times. Instead:
1. Learn each **pattern** once (its trigger, template, complexity, trap).
2. Master **2 anchor problems** per pattern cold — 38 problems, not 75.
3. Drill **recognition** (problem → pattern in <2 min) and **recall** (template from memory).
4. Repetition on a spaced schedule makes it obvious. Every other Blind 75 problem is
   then a same-pattern rep, not new learning.

## The files (read in this order)
| File | What it is | When you use it |
|---|---|---|
| `00_pattern_cards.md` | The 19 patterns: trigger, why, template, complexity, anchors, trap | Learn + review daily |
| `01_template_bank.py` | Runnable, tested Python skeletons — memorize these | Type from memory each day; run to verify |
| `02_anchor_problems.md` | 38 anchors (2/pattern) + every Blind 75 mapped to a pattern | Your solve queue |
| `03_decision_tree.md` | Problem → pattern in <2 min; constraint→complexity table; trigger words | Run at the start of every solve |
| `04_drill_schedule.md` | Front-load install (~2–3 wks) then spaced-repetition loop | Your daily plan |
| `05_interview_mode.md` | The live 5-phase protocol + self-scorecard | Every timed solve + real interview |

## Quick start (today)
1. Run the template bank to confirm it's correct:
   ```bash
   python3 patterns/01_template_bank.py     # expect: ALL TEMPLATES PASS
   ```
2. Read `00_pattern_cards.md` end to end once (~20 min) for the map.
3. Start `04_drill_schedule.md` Phase A, Day 1: Hashing + Two Pointers.
4. Log each anchor you solve in its own folder (kebab-case), same format as `../two-sum/`.

## Definition of interview-ready
- Identify the pattern of an unseen problem in **< 2 min**.
- Type the pattern's template from memory in **< 2 min**.
- Solve a medium end-to-end in **< 25 min**, testing all 4 categories, talking throughout.
- Then keep the Phase B spaced-repetition loop running while you apply.

---

## Python imports — know these cold (folded in from the long track)
```python
from collections import defaultdict, Counter, deque, OrderedDict
from typing import List, Optional, Tuple, Dict, Set
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from functools import lru_cache, cache
from itertools import combinations, permutations, product
from math import inf, gcd, ceil, floor, log2, sqrt
import sys                                  # sys.maxsize, sys.setrecursionlimit
# from sortedcontainers import SortedList   # external; handy for order-stat problems
```

## Python gotchas that fail hidden tests
- `list.pop(0)` is O(n) → use `deque.popleft()` (O(1)) for BFS queues.
- `heapq` is a **min-heap**; negate values for a max-heap.
- Default recursion limit ~1000 → `sys.setrecursionlimit(10**6)` for deep trees/DFS.
- Mutable default args are shared — never `def f(x, acc=[])`.
- Integer division `//` floors toward negative infinity; watch negatives.
- Append a **copy** in backtracking (`path[:]`), not the live list.
