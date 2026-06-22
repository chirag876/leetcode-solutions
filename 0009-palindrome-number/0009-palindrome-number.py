class Solution(object):

    def isPalindrome(self, x):
        # Store the original number so we can compare it later
        original = x

        # Variable to build the reversed number
        rev = 0

        # Extract digits one by one until the number becomes 0
        while x > 0:

            # Get the last digit of the number
            ld = x % 10

            # Append the last digit to the reversed number
            # Example:
            # rev = 12, ld = 3
            # rev becomes 123
            rev = rev * 10 + ld

            # Remove the last digit from the number
            x = x // 10

        # A number is a palindrome if the original
        # number and the reversed number are the same
        return original == rev

# class Solution(object):

    # def isPalindrome(self, x):
    #     """
    #     Check whether a number is a palindrome using string conversion.

    #     Approach:
    #     1. Convert the number to a string.
    #     2. Reverse the string using slicing [::-1].
    #     3. Compare the original string with the reversed string.

    #     Example:
    #     x = 121

    #     str(x)       -> "121"
    #     str(x)[::-1] -> "121"

    #     Since both strings are equal, the number is a palindrome.

    #     Time Complexity: O(n)
    #     Space Complexity: O(n)

    #     where n is the number of digits in the number.
    #     """

    #     # Convert the number to a string
    #     num_str = str(x)

    #     # Compare the original string with its reversed version
    #     return num_str == num_str[::-1]