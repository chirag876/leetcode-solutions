# 238. Product of Array Except Self

**Difficulty:** Medium  
**Topics:** Array, Prefix Sum, Prefix and Suffix Products

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

### Requirements

- The solution must run in `O(n)` time.
- The division operation must not be used.
- **Follow-up:** Can you solve it using `O(1)` extra space complexity? The output array does not count as extra space.

## Examples

### Example 1

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```python
[24, 12, 8, 6]
```

**Explanation:**

- Index 0: `2 × 3 × 4 = 24`
- Index 1: `1 × 3 × 4 = 12`
- Index 2: `1 × 2 × 4 = 8`
- Index 3: `1 × 2 × 3 = 6`

### Example 2

**Input:**
```python
nums = [-1, 1, 0, -3, 3]
```

**Output:**
```python
[0, 0, 9, 0, 0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- Each resulting `answer[i]` is guaranteed to fit in a 32-bit integer.

## Approach

**Brute Force**

For every index `i`, traverse the entire array using another loop. Skip the element at index `i`, multiply all the remaining elements, and append the product to the result array.

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(n)` for the output array.

**Limitation:** This approach may exceed the time limit for large inputs.

## Files

- `product_except_self.py` — Python implementation and practice solutions.

## LeetCode

Problem 238: Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
