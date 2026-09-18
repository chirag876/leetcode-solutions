class Solution(object):
    def isValid(self, s):
        stc = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in "({[":
                stc.append(char)
            else:
                if not stc:
                    return False
                if stc[-1] != pairs[char]:
                    return False
                stc.pop()
        return len(stc) == 0

        