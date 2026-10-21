
class Solution(object):
    def compress(self, chars):
        if not chars:
            return 0

        current_char = chars[0]
        count = 0
        out = ""

        for i in range(len(chars)):
            if current_char == chars[i]:
                count += 1
            else:
                out += current_char
                if count > 1:
                    out += str(count)

                current_char = chars[i]
                count = 1

        out += current_char
        if count > 1:
            out += str(count)

        chars[:] = list(out)

        return len(chars)
