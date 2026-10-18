
class Solution(object):
    def isValid(self, s):
        # Create an empty stack to store opening brackets.
        stc = []

        # Map each closing bracket to its corresponding opening bracket.
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # Iterate through each character in the input string.
        for char in s:

            # If the character is an opening bracket, push it onto the stack.
            if char in "({[":
                stc.append(char)

            else:
                # If the stack is empty, there is no opening bracket to match.
                if not stc:
                    return False

                # Check whether the top opening bracket matches the current closing bracket.
                if stc[-1] != pairs[char]:
                    return False

                # Remove the matched opening bracket from the top of the stack.
                stc.pop()

        # Return True if all opening brackets have been matched; otherwise, return False.
        return len(stc) == 0
