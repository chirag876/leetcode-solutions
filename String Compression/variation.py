# Variation 1 — Compress only if the result is shorter
def stringcompression(strs):

	current_char = strs[0]
	count = 0
	out = ""
	for char in range(len(strs)):
		if strs[char] == current_char:
			count += 1
		else:
			out += current_char + str(count)
			current_char = strs[char]
			count = 1
	out += current_char + str(count)
	print(len(out))
	print(len(strs))
	if len(out) < len(strs):
		return out
	else:
		return strs

strs = "AAABBCBCCCDD"
print(stringcompression(strs))


# Variation 2 — Decompress a compressed string
def decompress(strs):
    arr = list(strs)
    out = ""

    for i in range(0, len(arr), 2):
        char = arr[i]

        if i + 1 < len(arr):
            count = int(arr[i + 1])
        else:
            count = 1

        out += char * count

    return out


print(decompress("A3B2D"))

# Variation 3 — Case-insensitive compression
def stringcompression(strs):
	strs = strs.lower()
	current_char = strs[0]
	count = 0
	out = ""
	for char in range(len(strs)):
		if strs[char] == current_char:
			count += 1
		else:
			out += current_char + str(count)
			current_char = strs[char]
			count = 1
	out += current_char + str(count)
	return out

strs = "aaAAAbbB"
print(stringcompression(strs))

# NOTES : variation 3 can also be done for upper case as well


# Variation 4 — Compress using counts only when repeated
def stringcompression(strs):
	current_char = strs[0]
	count = 0
	out = ""
	for char in range(len(strs)):
		if strs[char] == current_char:
			count += 1
		else:
			out += current_char
			if count > 1:
				out += str(count)
			current_char = strs[char]
			count = 1
			
	out += current_char
	if count > 1:
		out += str(count)
	return out

strs = "AAABCDDD"
print(stringcompression(strs))