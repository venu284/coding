# DSA Study Plan — Neetcode + Concept-First Learning

> **This is the LONG TRACK (reference).** For the fast-pace, pattern-first system —
> the primary plan — see [`patterns/`](patterns/README.md). Use this doc for deeper
> concept notes and extra problems; follow `patterns/` where the two differ.

**Duration:** 26 weeks (6 months)
**Weekly commitment:** ~10 hours (1–2 hrs weekdays, 2–3 hrs weekends)
**Target:** 300+ problems, interview-ready
**Language:** Python

---

## How This Plan Works

This plan uses **Neetcode's Blind 75 → 150** as the problem backbone, but layers in **concept-first learning** (understand the "why" before solving) and **from-scratch practice** (write every solution like a real interview).

### The 4-Step Daily Routine (Every Single Problem)

```
Step 1: LEARN THE CONCEPT (15 min)
   → Understand WHY this pattern works, not just HOW
   → Ask Claude to teach the concept with visual examples

Step 2: SOLVE ON LEETCODE (20–30 min)
   → Get it passing, understand the approach
   → Read the editorial if stuck after 20 min

Step 3: REWRITE FROM SCRATCH (10–15 min)
   → Close LeetCode completely
   → Open a blank .py file
   → Write: imports → function with type hints → test cases
   → This is the step that makes you interview-ready

Step 4: LOG THE PATTERN (2 min)
   → One line: "Problem X → Pattern Y because Z"
   → Example: "3Sum → Two Pointers because sorted array + pair finding"
   → This log becomes your revision sheet in Phase 3
```

### From-Scratch Template

```python
# 1. Imports — know what you need without googling
from collections import defaultdict, Counter, deque
from typing import List, Optional
import heapq

# 2. Clean function with type hints
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# 3. Test cases — the part that impresses interviewers
if __name__ == "__main__":
    # Happy path
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Negative numbers
    assert two_sum([-1, -2, -3, -4, -8], -6) == [1, 3]

    # Duplicates
    assert two_sum([3, 3], 6) == [0, 1]

    # Minimum input
    assert two_sum([1, 2], 3) == [0, 1]

    print("All tests passed!")
```

### Test Case Categories (Cover All 4 Every Time)
1. **Happy path** — the example from the problem
2. **Edge case** — empty input, single element, all same values
3. **Boundary** — minimum/maximum constraints
4. **Tricky** — negatives, duplicates, already sorted, reverse sorted

---

## Phase 1: Blind 75 Core Patterns (Weeks 1–8)

> Goal: Learn all 15 DSA topics through Neetcode's curated 75 problems.
> Every problem follows the 4-step routine above.

### Week 1 — Arrays and Hashing

**Concepts to learn first:**
- Big-O notation (O(1), O(n), O(n²), O(log n), O(n log n))
- Hash maps and hash sets — why O(1) lookup matters
- Frequency counting with Counter and defaultdict
- Python list performance: list.pop(0) is O(n), deque.popleft() is O(1)

**Blind 75 problems (9):**
- [1] Two Sum
- [1] Contains Duplicate
- [1] Valid Anagram
- [1] Group Anagrams
- [1] Top K Frequent Elements
- [1] Product of Array Except Self
- [ ] Valid Sudoku
- [ ] Encode and Decode Strings
- [1] Longest Consecutive Sequence

**Pattern trigger:** "Find/count/group" → hash map. "O(n²) brute force with nested loops" → hash map makes it O(n).

---

### Week 2 — Two Pointers + Sliding Window

**Concepts to learn first:**
- Two pointers: opposite ends (sorted array), same direction (fast/slow)
- Sliding window: fixed size vs variable size
- When to shrink vs expand the window
- The "while left < right" template

**Blind 75 — Two Pointers (5):**
- [1] Valid Palindrome
- [1] Two Sum II (Input Array Is Sorted)
- [1] 3Sum
- [1] Container With Most Water
- [ ] Trapping Rain Water

**Blind 75 — Sliding Window (4):**
- [ ] Best Time to Buy and Sell Stock
- [ ] Longest Substring Without Repeating Characters
- [ ] Longest Repeating Character Replacement
- [ ] Minimum Window Substring

**Pattern triggers:**
- "Sorted array + find pair" → two pointers
- "Contiguous subarray/substring" → sliding window
- "Maximum/minimum length subarray with condition" → variable sliding window

---

### Week 3 — Stacks + Binary Search

**Concepts to learn first:**
- Stack: LIFO, Python list as stack (append/pop)
- Monotonic stack: maintains increasing/decreasing order
- Binary search: the lo/hi template, why `lo + (hi - lo) // 2` prevents overflow
- Binary search on answer space (not just sorted arrays)
- Python bisect module

**Blind 75 — Stack (3):**
- [ ] Valid Parentheses
- [ ] Min Stack
- [ ] Evaluate Reverse Polish Notation

**Blind 75 — Binary Search (2):**
- [ ] Binary Search
- [ ] Search in Rotated Sorted Array

**Bonus practice (3):**
- [ ] Daily Temperatures (monotonic stack)
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Search a 2D Matrix

**Pattern triggers:**
- "Next greater/smaller element" → monotonic stack
- "Matching brackets/parentheses" → stack
- "Sorted or rotated sorted + find" → binary search
- "Minimize the maximum / maximize the minimum" → binary search on answer

---

### Week 4 — Linked Lists

**Concepts to learn first:**
- Node class implementation in Python
- Pointer manipulation — draw before you code
- Dummy head node pattern (eliminates edge cases)
- Fast/slow pointer technique (Floyd's cycle detection)
- Reversal: iterative (prev, curr, next) and recursive

**Blind 75 (6):**
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Linked List Cycle
- [ ] Reorder List
- [ ] Remove Nth Node From End of List
- [ ] Merge K Sorted Lists

**Pattern triggers:**
- "Middle of linked list" → fast/slow pointers
- "Cycle detection" → fast/slow pointers
- "Merge sorted lists" → dummy head + comparison
- "Reverse" → prev/curr/next iterative pattern

---

### Week 5 — Trees (Fundamentals)

**Concepts to learn first:**
- Binary tree vs BST (BST property: left < root < right)
- Traversals: inorder (sorted for BST), preorder (root first), postorder (children first)
- BFS with deque (level-order traversal)
- Recursive tree pattern: base case → recurse left → recurse right → combine
- Height vs depth

**Blind 75 (7):**
- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Same Tree
- [ ] Subtree of Another Tree
- [ ] Lowest Common Ancestor of BST
- [ ] Binary Tree Level Order Traversal
- [ ] Validate Binary Search Tree

**Pattern trigger:** Most tree problems = "what info do I need from left subtree and right subtree?" Think bottom-up recursion.

---

### Week 6 — Trees (Advanced) + Heaps

**Concepts to learn first:**
- Constructing trees from traversal arrays
- Tree serialization/deserialization
- BST operations (insert, delete, search)
- Heap: complete binary tree, min-heap property
- Python heapq: heappush, heappop, nlargest, nsmallest
- Max-heap trick: negate all values

**Blind 75 — Trees part 2 (4):**
- [ ] Kth Smallest Element in a BST
- [ ] Construct Binary Tree from Preorder and Inorder
- [ ] Binary Tree Maximum Path Sum
- [ ] Serialize and Deserialize Binary Tree

**Blind 75 — Heap (1):**
- [ ] Find Median from Data Stream

**Pattern triggers:**
- "Kth largest/smallest" → heap (size K)
- "Top K" → min-heap of size K
- "Streaming data + median" → two heaps
- "BST + sorted order" → inorder traversal

---

### Week 7 — Graphs (BFS/DFS)

**Concepts to learn first:**
- Graph representations: adjacency list (defaultdict(list)), adjacency matrix
- DFS: recursive + iterative (with stack)
- BFS: with deque, level-by-level processing
- Visited set to prevent infinite loops
- Grid as graph: 4 directions = [(0,1),(0,-1),(1,0),(-1,0)]
- Connected components
- Cycle detection (directed: recursion stack, undirected: visited parent)

**Blind 75 (6):**
- [ ] Number of Islands
- [ ] Clone Graph
- [ ] Pacific Atlantic Water Flow
- [ ] Course Schedule
- [ ] Number of Connected Components in an Undirected Graph
- [ ] Graph Valid Tree

**Pattern triggers:**
- "Grid + connected regions" → BFS/DFS flood fill
- "Prerequisites/dependencies" → directed graph + topological sort
- "Shortest path (unweighted)" → BFS
- "Explore all paths" → DFS

---

### Week 8 — Dynamic Programming (1D)

**Concepts to learn first:**
- Two properties: overlapping subproblems + optimal substructure
- Memoization (top-down): recursion + cache
- Tabulation (bottom-up): iterative + array
- State definition: what changes between subproblems?
- Recurrence relation: how does dp[i] relate to previous states?
- Space optimization: rolling array when dp[i] only depends on dp[i-1]

**Blind 75 (10):**
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Longest Increasing Subsequence
- [ ] Coin Change
- [ ] Word Break
- [ ] Combination Sum IV
- [ ] Decode Ways
- [ ] Unique Paths
- [ ] Jump Game

**Pattern triggers:**
- "How many ways" → DP (counting)
- "Minimum/maximum cost/value" → DP (optimization)
- "Can you reach / is it possible" → DP (feasibility)
- "Subsequence" → often DP or binary search

**Approach for every DP problem:**
1. Define the state: what does dp[i] represent?
2. Write the recurrence: dp[i] = f(dp[i-1], dp[i-2], ...)
3. Identify base cases: dp[0] = ?, dp[1] = ?
4. Determine iteration order
5. Optimize space if possible

---

## Phase 2: Neetcode 150 Expansion (Weeks 9–13)

> Goal: Fill gaps Blind 75 leaves. Add depth to every topic.
> You already know the patterns — now build fluency with more reps.

### Week 9 — Arrays, Strings, Hashing Depth

**New patterns:** Prefix/suffix products, bucket sort, matrix operations, encode/decode.

**Neetcode 150 extras (~10):**
- [ ] Valid Palindrome II
- [ ] 3Sum Closest
- [ ] Sort Colors (Dutch National Flag)
- [ ] Next Permutation
- [ ] Rotate Image
- [ ] Spiral Matrix
- [ ] Set Matrix Zeroes
- [ ] String to Integer (atoi)
- [ ] Longest Common Prefix
- [ ] Plus One

---

### Week 10 — Stacks, Binary Search, Sliding Window Depth

**New patterns:** Monotonic stack for histograms, binary search on answer space, advanced sliding window.

**Neetcode 150 extras (~12):**
- [ ] Largest Rectangle in Histogram
- [ ] Car Fleet
- [ ] Koko Eating Bananas
- [ ] Find Peak Element
- [ ] Time Based Key-Value Store
- [ ] Permutation in String
- [ ] Sliding Window Maximum
- [ ] Generate Parentheses
- [ ] Asteroid Collision
- [ ] Capacity to Ship Packages Within D Days
- [ ] Find Minimum in Rotated Sorted Array II
- [ ] Minimum Size Subarray Sum

---

### Week 11 — Linked Lists, Trees, Tries Depth

**New patterns:** Trie (prefix tree), wildcard search, deep copy with random pointers, tree path problems.

**Neetcode 150 extras (~12):**
- [ ] Implement Trie (Prefix Tree)
- [ ] Design Add and Search Words Data Structure
- [ ] Word Search II
- [ ] Copy List with Random Pointer
- [ ] Add Two Numbers
- [ ] LRU Cache
- [ ] Count Good Nodes in Binary Tree
- [ ] Diameter of Binary Tree
- [ ] Balanced Binary Tree
- [ ] Path Sum III
- [ ] Binary Tree Right Side View
- [ ] House Robber III (tree DP)

---

### Week 12 — Graphs, Advanced Graphs, Heaps Depth

**New patterns:** Topological sort (Kahn's), Union-Find, Dijkstra's, multi-source BFS, two-heap.

**Neetcode 150 extras (~12):**
- [ ] Alien Dictionary
- [ ] Cheapest Flights Within K Stops
- [ ] Network Delay Time
- [ ] Redundant Connection
- [ ] Walls and Gates
- [ ] Rotting Oranges
- [ ] Surrounded Regions
- [ ] Task Scheduler
- [ ] K Closest Points to Origin
- [ ] Reorganize String
- [ ] Swim in Rising Water
- [ ] Min Cost to Connect All Points

---

### Week 13 — DP, Backtracking, Greedy, Intervals, Bits (Heavy Week)

**New patterns:** 2D DP, backtracking decision trees, greedy choice property, interval scheduling, bit tricks.

> This is a heavy week. Stretch to 12–15 hours if needed. These are the remaining Neetcode 150 topics.

**Neetcode 150 extras (~18):**

*2D DP:*
- [ ] Longest Common Subsequence
- [ ] Edit Distance
- [ ] Target Sum
- [ ] Interleaving String

*Backtracking:*
- [ ] Subsets / Subsets II
- [ ] Permutations
- [ ] Combination Sum / Combination Sum II
- [ ] Palindrome Partitioning
- [ ] Letter Combinations of Phone Number
- [ ] N-Queens

*Greedy:*
- [ ] Jump Game II
- [ ] Gas Station
- [ ] Hand of Straights

*Intervals:*
- [ ] Merge Intervals
- [ ] Insert Interval
- [ ] Non-overlapping Intervals

*Bit Manipulation:*
- [ ] Single Number
- [ ] Number of 1 Bits
- [ ] Counting Bits
- [ ] Reverse Bits
- [ ] Missing Number

---

## Phase 3: Mastery and Interview Readiness (Weeks 14–26)

> Goal: Pattern recognition under pressure. Timed solving. Mock interviews.
> No more topic labels — identify the pattern yourself.

### Weeks 14–15 — Review Sprint: Arrays through Trees
- Re-solve 20 medium/hard problems from Phase 1 (weeks 1–6)
- Time yourself: 25 min/medium, 40 min/hard
- All from-scratch format
- Track: Did you identify the pattern in under 3 minutes?

### Weeks 16–17 — Review Sprint: Graphs through DP
- Re-solve 20 medium/hard problems from Phase 1 (weeks 7–8) and Phase 2
- Focus on DP recurrence relations and graph traversal choices
- Write recurrence BEFORE coding for every DP problem

### Weeks 18–19 — Blind Pattern Recognition
- Solve 20 random LeetCode mediums WITHOUT topic labels
- Method: Read → identify pattern (3 min) → plan (5 min) → code (20 min) → test
- After each: write which clue in the problem pointed to the pattern
- Build your "trigger word" vocabulary

### Weeks 20–21 — Hard Problem Deep-Dive
- Solve 12–15 hard problems combining multiple patterns
- Must-solve: Trapping Rain Water, Sliding Window Maximum, Merge K Sorted Lists, Word Ladder, Alien Dictionary, Burst Balloons, Median of Two Sorted Arrays, Minimum Window Substring, Word Search II, Serialize/Deserialize Binary Tree
- Method: 45 min attempt → study editorial → implement without looking → re-solve next day

### Week 22 — OOP and System Design Basics
- Design patterns for coding interviews (not full system design)
- Practice: LRU Cache, LFU Cache, Min Stack, Design Twitter, Design HashSet/HashMap
- Focus on clean class structure, encapsulation, readable code

### Weeks 23–24 — Full Mock Interviews
- 4–5 complete mock interviews (2 problems each, 45–50 min)
- Format: Clarify → approach + complexity → code → test → optimize
- Practice explaining your thinking OUT LOUD
- Prepare 3–4 STAR behavioral stories

### Week 25 — Weak Spot Targeted Practice
- Review your pattern log from the entire plan
- Identify 3 weakest topics by "time to identify pattern"
- Solve 5 new problems in each weak topic
- Re-verify from-scratch test case coverage

### Week 26 — Final Prep
- 2 final mock interviews
- Speed-review top 30 problems (pattern + approach only, code if rusty)
- Confidence checklist:
  - [ ] Can explain all 15 topics in 2 sentences each
  - [ ] Can identify patterns in under 3 minutes
  - [ ] Can write clean from-scratch code in 20 minutes
  - [ ] Have 3 STAR stories ready
  - [ ] Comfortable with Python imports, type hints, and testing

---

## Quick Reference: Pattern Trigger Words

| Trigger in Problem | Pattern to Try |
|---|---|
| "Find pair/group" | Hash map |
| "Sorted array + pair" | Two pointers |
| "Contiguous subarray" | Sliding window |
| "Matching/nesting" | Stack |
| "Next greater/smaller" | Monotonic stack |
| "Sorted + find" | Binary search |
| "Minimize max / maximize min" | Binary search on answer |
| "Linked list middle/cycle" | Fast/slow pointers |
| "Tree + subtree info" | DFS recursion (bottom-up) |
| "Level-by-level" | BFS with deque |
| "Prefix matching" | Trie |
| "Top K / streaming" | Heap |
| "Connected regions / grid" | BFS/DFS flood fill |
| "Dependencies / ordering" | Topological sort |
| "Shortest path (weighted)" | Dijkstra's |
| "Group connectivity" | Union-Find |
| "How many ways" | DP (counting) |
| "Min/max cost" | DP (optimization) |
| "All combinations/subsets" | Backtracking |
| "Interval overlap" | Sort by start, merge |
| "Bitwise tricks" | XOR, AND, shifts |

---

## Python Imports Cheat Sheet (Know These Cold)

```python
from collections import defaultdict, Counter, deque, OrderedDict
from typing import List, Optional, Tuple, Dict, Set
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from functools import lru_cache, cache
from itertools import combinations, permutations, product
from math import inf, gcd, ceil, floor, log2, sqrt
from sortedcontainers import SortedList  # external but useful
import sys  # for sys.maxsize, sys.setrecursionlimit
```

---
