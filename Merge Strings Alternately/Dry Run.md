# Merge Alternately - Dry Run

## Problem

Merge two strings by taking one character from each string alternately.
If one string is longer, append the remaining characters at the end.

------------------------------------------------------------------------

## Example

``` text
word1 = "abc"
word2 = "pqrs"
```

### Step 1

``` python
n = min(len(word1), len(word2))
```

-   `len(word1) = 3`
-   `len(word2) = 4`
-   `n = 3`

**Why?**

We only want to iterate while **both** strings still have characters.
Using the smaller length prevents an index out of range error.

------------------------------------------------------------------------

### Step 2

Initial value:

``` text
result = ""
```

------------------------------------------------------------------------

### Step 3

Loop:

#### Iteration 1 (`i = 0`)

``` text
result += word1[0]   -> "a"
result += word2[0]   -> "p"

result = "ap"
```

------------------------------------------------------------------------

#### Iteration 2 (`i = 1`)

``` text
result += word1[1]   -> "b"
result += word2[1]   -> "q"

result = "apbq"
```

------------------------------------------------------------------------

#### Iteration 3 (`i = 2`)

``` text
result += word1[2]   -> "c"
result += word2[2]   -> "r"

result = "apbqcr"
```

The loop ends because `i` has reached `n - 1`.

------------------------------------------------------------------------

### Step 4

Append the remaining characters.

``` python
result += word1[n:]
result += word2[n:]
```

Evaluate the slices:

``` text
word1[3:] -> ""
word2[3:] -> "s"
```

Result becomes:

``` text
"apbqcr" + "" + "s"
= "apbqcrs"
```

------------------------------------------------------------------------

## Final Output

``` text
apbqcrs
```

------------------------------------------------------------------------

## Key Takeaways

-   `n` is the minimum length, so the loop never accesses an invalid
    index.
-   `word1[n:]` and `word2[n:]` return the remaining characters.
-   If nothing is left, Python returns an empty string (`""`), so no
    `if-else` is needed.
