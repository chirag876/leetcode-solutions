class Solution(object):
    def groupAnagrams(self, strs):
        # Create an empty dictionary to store groups of anagrams.
        # Key   -> Sorted version of the word (e.g., "aet")
        # Value -> List of words that have the same sorted characters.
        group = {}

        # Iterate through each word in the input list.
        for word in strs:

            # Sort the characters of the current word alphabetically.
            # Since anagrams contain the same letters, they will produce
            # the same sorted string.
            #
            # Example:
            # "eat" -> ['a', 'e', 't'] -> "aet"
            # "tea" -> ['a', 'e', 't'] -> "aet"
            # "ate" -> ['a', 'e', 't'] -> "aet"
            #
            # This sorted string acts as the unique key.
            key = ''.join(sorted(word))

            # Check whether this sorted key already exists
            # in the dictionary.
            if key not in group:

                # If the key does not exist, create a new empty list
                # to store all words that belong to this anagram group.
                group[key] = []

            # Append the current word to its corresponding anagram group.
            group[key].append(word)

        # The dictionary values contain all grouped anagrams.
        #
        # Example dictionary:
        # {
        #     "aet": ["eat", "tea", "ate"],
        #     "ant": ["tan", "nat"],
        #     "abt": ["bat"]
        # }
        #
        # We only need the grouped lists, not the keys.
        # Therefore, return all dictionary values as a list.
        return list(group.values())