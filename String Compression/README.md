# String Compression Problem

## Problem Statement

Given a string consisting of uppercase alphabetic characters, compress
the string by replacing consecutive occurrences of the same character
with the character followed by its count.

### Example

Input: `AAABBCCCCDAABBB`

Output: `A3B2C4D1A2B3`

## Constraints

-   The input string contains only uppercase English letters (`A-Z`).
-   The length of the string is greater than 0.
-   Consecutive characters should be grouped together and counted.
-   The output should preserve the order of appearance of characters.

## Notes

-   This problem follows the Run Length Encoding (RLE) approach.
-   Each group of consecutive characters is represented as:
    `character + count`
