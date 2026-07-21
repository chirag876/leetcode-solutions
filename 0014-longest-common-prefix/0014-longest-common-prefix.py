class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        fw = strs[0]
        for i in range(len(fw)):
            char = strs[0][i]
            for word in strs:
                if i >=len(word) or word[i] !=char:
                    return strs[0][:i]
        return fw
