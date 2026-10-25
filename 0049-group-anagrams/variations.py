## Variation 1 — Group Anagrams Case-Insensitively


def groupAnagrams(strs):
    group = {}

    for word in strs:
        key = ''.join(sorted(word.upper()))

        if key not in group:
            group[key] = []

        group[key].append(word)

    return list(group.values())


strs = ["Eat", "tea", "ATE", "bat", "Tab", "NAT", "Tan"]
print(groupAnagrams(strs))


## Variation 2 — Return All Largest Anagram Groups


def groupAnagrams(strs):
    group = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in group:
            group[key] = []

        group[key].append(word)

    groups = list(group.values())
    max_len = max(len(g) for g in groups)

    return [g for g in groups if len(g) == max_len]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

# Tie example: both groups of size 2 must be returned.
strs = ["ab", "ba", "cd", "dc", "ef"]
print(groupAnagrams(strs))


## Variation 3 — Group Anagrams Without Sorting


def groupAnagrams(strs):
    group = {}

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)

        if key not in group:
            group[key] = []

        group[key].append(word)

    return list(group.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


## Variation 4 — Return Only Groups Containing at Least Two Strings


def groupAnagrams(strs):
    group = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in group:
            group[key] = []

        group[key].append(word)

    group2 = list(group.values())
    lon_len = []

    for i in range(len(group2)):
        if len(group2[i]) >= 2:
            lon_len.append(group2[i])

    return lon_len


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


## Variation 5 — Sort the Strings Within Each Group


def groupAnagrams(strs):
    out = []
    group = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in group:
            group[key] = []

        group[key].append(word)

    group2 = list(group.values())

    for i in range(len(group2)):
        out.append(sorted(group2[i]))

    return out


strs = ["eat", "tea", "ate", "bat"]
print(groupAnagrams(strs))
