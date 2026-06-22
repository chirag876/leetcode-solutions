class Solution(object):
    
    def isPalindrome(self, x):
        original = x
        rev = 0
        while x > 0:
            ld = x%10
            rev = rev*10+ld
            x = x//10
        return original == rev
            
