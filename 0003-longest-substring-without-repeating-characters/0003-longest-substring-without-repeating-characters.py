class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Set to store the unique characters present in the current window
        char = set()

        # Left pointer represents the starting position of the current window
        left = 0

        # Stores the maximum length found so far
        max_len = 0

        # Right pointer moves through the string one character at a time
        for right in range(len(s)):

            # If the current character already exists in the window,
            # shrink the window from the left until the duplicate is removed
            while s[right] in char:

                # Remove the character at the left pointer from the set
                char.remove(s[left])

                # Move the left pointer one position to the right
                left += 1

            # Add the current character to the set
            # Now the current window contains only unique characters
            char.add(s[right])

            # Calculate the current window length:
            # right - left + 1
            # and update max_len if the current window is larger
            max_len = max(max_len, right - left + 1)

        # Return the length of the longest substring without repeating characters
        return max_len