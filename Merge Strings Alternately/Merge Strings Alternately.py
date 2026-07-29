class Solution(object):
    def mergeAlternately(self, word1, word2):

        # Store the final merged string.
        result = ""

        # Find the length of the shorter string.
        # We can only alternate characters while both strings have characters.
        n = min(len(word1), len(word2))

        # Traverse both strings up to the shorter length.
        for i in range(n):

            # Append one character from the first string.
            result += word1[i]

            # Append one character from the second string.
            result += word2[i]

        # Append any remaining characters from word1.
        # If there are none, this adds an empty string.
        result += word1[n:]

        # Append any remaining characters from word2.
        # If there are none, this also adds an empty string.
        result += word2[n:]

        # Return the merged string.
        return result