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
