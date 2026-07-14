class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1 # start from the end

        # skip the trailing spaces 
        while i >= 0 and s[i] == " ":
            i -=1
        
        count = 0

        # count the last word
        while i >= 0 and s[i] !=" ":
            count +=1
            i -=1
        return count