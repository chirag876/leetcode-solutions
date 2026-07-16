def strscompression(char):
    current_char = char[0]
    count = 0
    out = ""

    for i in range(len(char)):
        if char[i] == current_char:
            count += 1
        else:
            out += current_char + str(count)
            current_char = char[i]
            count = 1

    out += current_char + str(count)
    return out


text = "AAABBCCCCDAABBB"
print(strscompression(text))
