# LeetCode Practice Repo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a lightweight Python LeetCode practice repository with a global README, reusable problem README template, and initial `two-sum` problem folder.

**Architecture:** The repo is documentation-first and folder-based. Each problem lives in a kebab-case folder named from the LeetCode title and contains a Python solution plus reflection README.

**Tech Stack:** Markdown, Python 3 standard syntax.

---

## File Structure

- Create: `README.md` for repository purpose, workflow, naming convention, and layout.
- Create: `templates/problem-readme.md` for reusable learning and reflection notes.
- Create: `two-sum/README.md` as the first problem README using the template sections.
- Create: `two-sum/solution.py` as a minimal Python LeetCode solution skeleton.

### Task 1: Global README And Template

**Files:**
- Create: `README.md`
- Create: `templates/problem-readme.md`

- [ ] **Step 1: Create `README.md`**

````markdown
# LeetCode Practice

Daily LeetCode practice repository for Python solutions, notes, and reflections.

Each problem has its own folder named after the problem title using lowercase kebab-case.

## Layout

```text
.
├── README.md
├── templates/
│   └── problem-readme.md
└── problem-title/
    ├── README.md
    └── solution.py
```

## Daily Workflow

1. Solve a LeetCode problem.
2. Create a folder using the problem title, such as `two-sum`.
3. Add the accepted Python solution in `solution.py`.
4. Copy `templates/problem-readme.md` into the problem folder as `README.md`.
5. Record the approach, mistakes, edge cases, learnings, and reflections.

## Naming Convention

Use lowercase kebab-case based on the LeetCode title:

- `Two Sum` -> `two-sum`
- `Valid Parentheses` -> `valid-parentheses`
- `Best Time to Buy and Sell Stock` -> `best-time-to-buy-and-sell-stock`

If two titles normalize to the same folder name, append a short disambiguator.

## Problem Folder Checklist

- `README.md` contains notes, learnings, and reflections.
- `solution.py` contains the Python solution submitted or practiced.
- Complexity analysis is recorded after solving.
- Any mistakes or edge cases are written down while still fresh.
````

- [ ] **Step 2: Create `templates/problem-readme.md`**

````markdown
# Problem Title

## Problem

- Link:
- Difficulty:
- Date solved:
- Topics:

## Summary

Write a short summary of what the problem asks.

## Approach

Describe the core idea in your own words.

## Algorithm

1. Describe the first key step.
2. Describe the second key step.
3. Describe how the result is returned.

## Complexity

- Time:
- Space:

## Key Learnings

- Record the most important concept or pattern learned.
- Note any Python-specific technique that helped.

## Mistakes And Edge Cases

- Record mistakes made during the first attempt.
- List edge cases that are easy to miss.

## Reflection

What would make this problem easier to recognize next time?

## Follow-Up

- Alternative approach to try:
- Similar problems to practice:
````

- [ ] **Step 3: Verify files exist**

Run: `test -f README.md && test -f templates/problem-readme.md`

Expected: command exits with status 0.

### Task 2: Initial Two Sum Problem Folder

**Files:**
- Create: `two-sum/README.md`
- Create: `two-sum/solution.py`

- [ ] **Step 1: Create `two-sum/README.md`**

````markdown
# Two Sum

## Problem

- Link: https://leetcode.com/problems/two-sum/
- Difficulty: Easy
- Date solved:
- Topics: Array, Hash Table

## Summary

Given an array of integers and a target, return the indices of two numbers whose values add up to the target.

## Approach

Use a hash map to remember numbers already seen and their indices. For each number, compute the needed complement. If the complement has already been seen, return both indices.

## Algorithm

1. Create an empty dictionary from number to index.
2. Iterate through `nums` with each index and value.
3. Compute `target - value`.
4. If the complement is in the dictionary, return the stored index and current index.
5. Store the current value and index before moving to the next number.

## Complexity

- Time: O(n)
- Space: O(n)

## Key Learnings

- A hash map can turn a repeated lookup problem into a single pass.
- Store previous values before checking future values when pair order matters.

## Mistakes And Edge Cases

- Duplicate numbers can be valid when they appear at different indices.
- Do not reuse the same index twice.

## Reflection

This pattern is useful when a problem asks whether a matching value has appeared before.

## Follow-Up

- Alternative approach to try: sort with two pointers while preserving original indices.
- Similar problems to practice: 3Sum, Two Sum II, Subarray Sum Equals K.
````

- [ ] **Step 2: Create `two-sum/solution.py`**

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index

        return []
```

- [ ] **Step 3: Verify Python syntax**

Run: `python3 -m py_compile two-sum/solution.py`

Expected: command exits with status 0.

- [ ] **Step 4: Verify expected files exist**

Run: `test -f two-sum/README.md && test -f two-sum/solution.py`

Expected: command exits with status 0.
