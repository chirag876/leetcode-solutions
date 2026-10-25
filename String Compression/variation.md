# String Compression — Problem Variations

## Variation 1: Compress Only If the Result Is Shorter

### Description
Return the original string if the compressed string's length is not strictly shorter than the original string.

### Example

**Input:**
```text
ABCDE
```

**Output:**
```text
ABCDE
```

### Task
After compression, decide which result to return.

---

## Variation 2: Decompress a Compressed String

### Description
The input will be provided in compressed format. Reconstruct the original string according to the count given after each character.

Assume that a positive integer count is provided after every character.

### Example

**Input:**
```text
A3B2C4
```

**Output:**
```text
AAABBCCCC
```

### Task
Implement the counting and string reconstruction logic.

---

## Variation 3: Case-Insensitive Compression

### Description
Uppercase and lowercase versions of the same letter will be treated as one group, but the output will use the lowercase version of the group's first character.

### Example

**Input:**
```text
aaAAAbbB
```

**Output:**
```text
a5b3
```

### Task
Modify the character comparison logic and decide which character to preserve in the output. The output should use the lowercase version of the group's first character.

---

## Variation 4: Use Counts Only for Repeated Characters

### Description
Do not write a count for characters that occur only once. Include the count only when a character appears consecutively multiple times.

### Example

**Input:**
```text
AAABCDDD
```

**Output:**
```text
A3BCD3
```

### Task
Keep the grouping logic the same, but modify the condition for the output format.