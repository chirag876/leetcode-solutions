class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: If the input list is empty, there's no prefix to find.
        if not strs:
            return ""
        
        # We pick the first word as our reference point to compare against all others.
        fw = strs[0]
        
        # Loop through every character index of our reference word.
        # Example: "flower" -> i will be 0, 1, 2, 3, 4, 5
        for i in range(len(fw)):
            char = strs[0][i]  # The specific character we are comparing in this "column"
            
            # Now, compare this specific character against the same index in all other words.
            for word in strs:
                # Two conditions where we MUST stop:
                # 1. i >= len(word): The current word is shorter than our index 'i' (run out of letters).
                # 2. word[i] != char: The character at this position doesn't match our reference.
                if i >= len(word) or word[i] != char:
                    # If either condition is met, the prefix ends right BEFORE this index.
                    # We return the slice of the first word from 0 up to i.
                    return strs[0][:i]
        
        # If we finish the entire loop without hitting a mismatch, it means the 
        # entire first word IS the prefix (this happens if the first word is the 
        # shortest and matches the beginning of all others).
        return fw