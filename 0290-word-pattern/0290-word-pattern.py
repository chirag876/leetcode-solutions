class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Convert the sentence into a list of words
        s = s.split()

        # If the number of pattern characters and words are different,
        # they can never match
        if len(pattern) != len(s):
            return False

        # Dictionary to store:
        # character -> word
        char_word = {}

        # Dictionary to store:
        # word -> character
        # This is used to make sure one word cannot map to two characters
        word_char = {}

        # Go through every character and word together
        for i in range(len(pattern)):

            # Current character from the pattern
            ch = pattern[i]

            # Current word from the sentence
            word = s[i]

            # If both the character and the word already exist,
            # check if they still have the same mapping
            if ch in char_word and word in word_char:

                # If the stored word is different from the current word,
                # the pattern is broken
                if char_word[ch] != word:
                    return False

                # If the stored character is different from the current character,
                # the pattern is broken
                if word_char[word] != ch:
                    return False

            # If only one of them already exists,
            # it means the mapping is inconsistent
            elif ch in char_word or word in word_char:
                return False

            # Both character and word are new,
            # so create a new mapping in both dictionaries
            else:
                char_word[ch] = word
                word_char[word] = ch

        # If we finish the loop without any mismatch,
        # the pattern is valid
        return True