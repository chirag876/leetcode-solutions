# longest_substring_withoutrepeating_character_return_original_string
def lengthOfLongestSubstring(s):
	char = set()
	left = 0
	max_len = 0
	max_str_Start_index = 0
	for right in range(len(s)):
		while s[right] in char:
			char.remove(s[left])
			left += 1
		char.add(s[right])
		if right-left+1> max_len:
			max_len = right-left+1
			max_str_Start_index = left
	return s[max_str_Start_index:max_str_Start_index+max_len]

print(lengthOfLongestSubstring("abcabcbb"))