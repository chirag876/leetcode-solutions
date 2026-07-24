class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) !=len(s):
            return False
        char_word = {}
        word_char = {}
        for i in range(len(pattern)):
            ch = pattern[i]
            word = s[i]
            if ch in char_word and word in word_char:
                if char_word[ch] != word:
                     return False

                if word_char[word] != ch:
                     return False
            elif ch in char_word or word in word_char:
                return False
            else:
                char_word[ch] = word
                word_char[word] = ch
        return True