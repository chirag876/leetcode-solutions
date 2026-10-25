# Group Anagrams — Coding Interview Variations

Based on LeetCode 49: Group Anagrams.

## Standard Problem

Given an array of strings, group the anagrams together. The groups may be returned in any order.

### Standard Solution Complexity

Let:
- `n` = number of strings
- `k` = maximum length of a string

**Time Complexity: `O(n * k log k)`**

Each word is sorted to create its anagram key. Sorting a word of length at most `k` takes `O(k log k)`. Doing this for `n` words gives `O(n * k log k)` overall.

**Space Complexity: `O(n * k)`**

The dictionary stores the sorted keys and the words in their groups. Across all strings, this storage is bounded by `O(n * k)`, including the grouped output.

---

## Variation 1 — Group Anagrams Case-Insensitively

### Problem

Group strings that are anagrams when uppercase and lowercase letters are treated as equivalent. Preserve each string's original spelling in the output.

### Example

**Input**
```python
["Eat", "tea", "ATE", "bat", "Tab"]
```

**Possible output**
```python
[["Eat", "tea", "ATE"], ["bat", "Tab"]]
```

Group order and order within each group may vary.

### Expected Approach

Normalize each word to a common case when generating the key, but store the original word in the group.

### Complexity

- **Time:** `O(n * k log k)` — each normalized word is sorted.
- **Space:** `O(n * k)` — keys and grouped strings are stored.

---

## Variation 2 — Return All Largest Anagram Groups

### Problem

First group all anagrams. Then return only the groups whose size equals the maximum group size. If multiple groups tie for the largest size, return all of them.

### Example 1

**Input**
```python
["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Possible output**
```python
[["eat", "tea", "ate"]]
```

The group sizes are 3, 2, and 1, so only the group of size 3 is returned.

### Example 2 — Tie for Largest Group

**Input**
```python
["ab", "ba", "cd", "dc", "ef"]
```

**Possible output**
```python
[["ab", "ba"], ["cd", "dc"]]
```

Both groups have the maximum size of 2, so both must be returned.

### Expected Approach

1. Build the anagram groups.
2. Find the maximum group size.
3. Return every group whose size equals that maximum.

### Complexity

- **Time:** `O(n * k log k)` — grouping dominates; finding the maximum and filtering the groups take `O(n)` additional time.
- **Space:** `O(n * k)` — the dictionary and returned groups store the strings.

---

## Variation 3 — Group Anagrams Without Sorting

### Problem

Group anagrams without using `sorted()` or any sorting algorithm. The input contains only lowercase English letters (`a`–`z`).

For each word, create a key from the frequency of its 26 possible letters.

### Example

**Input**
```python
["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Possible output**
```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

The output can look the same as the standard solution. The change is the required algorithm: the key must be built from character frequencies, not sorting.

### Expected Approach

1. Create a 26-element frequency array for each word.
2. Increment the position corresponding to each character.
3. Convert the array to a tuple and use it as the dictionary key.
4. Add the original word to that group.

### Complexity

- **Time:** `O(n * k)` — count each character; creating and hashing the 26-element key takes constant time because 26 is fixed.
- **Space:** `O(n * k)` — the dictionary stores keys and grouped strings; each temporary frequency array has fixed size 26.

---

## Variation 4 — Return Only Groups Containing at Least Two Strings

### Problem

Group all anagrams, but return only groups that contain at least two strings. Exclude groups containing just one string.

### Example

**Input**
```python
["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Possible output**
```python
[["eat", "tea", "ate"], ["tan", "nat"]]
```

The group containing only `"bat"` is excluded.

### Expected Approach

Build all groups first, then filter out groups whose length is less than 2.

### Complexity

- **Time:** `O(n * k log k)` — grouping dominates; filtering groups takes `O(n)` additional time.
- **Space:** `O(n * k)` — the dictionary and returned groups store strings.

---

## Variation 5 — Sort the Strings Within Each Group

### Problem

Group anagrams as usual, but sort the strings inside each group in lexicographical order. The order of the groups themselves may be arbitrary.

### Example

**Input**
```python
["eat", "tea", "ate", "bat"]
```

**Possible output**
```python
[["ate", "eat", "tea"], ["bat"]]
```

### Expected Approach

Build the anagram groups, then sort the strings inside each group before returning the result.

### Complexity

- **Time:** `O(n * k log k)` — creating keys requires sorting each word. Sorting the members of all groups adds at most `O(n * k log n)` in a conservative bound, so the overall complexity can be stated as `O(n * k log(n + k))`.
- **Space:** `O(n * k)` — the dictionary and result store the grouped strings; sorting may use additional temporary space.

---

## Summary

| Variation | Main Change | Time Complexity | Space Complexity |
|---|---|---|---|
| 1. Case-insensitive | Normalize case for keys; preserve original strings | `O(n * k log k)` | `O(n * k)` |
| 2. All largest groups | Return every group tied for maximum size | `O(n * k log k)` | `O(n * k)` |
| 3. Without sorting | Use 26-letter frequency keys | `O(n * k)` | `O(n * k)` |
| 4. Groups of size ≥ 2 | Filter singleton groups | `O(n * k log k)` | `O(n * k)` |
| 5. Sort within groups | Sort each group's members | `O(n * k log(n + k))` | `O(n * k)` |

Here, `n` is the number of strings and `k` is the maximum string length.