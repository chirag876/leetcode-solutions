def strscompression(char):
    # Store the first character to start comparing with the rest.
    current_char = char[0]

    # Count how many times the current character appears consecutively.
    count = 0

    # Store the final compressed string.
    out = ""

    # Loop through every character in the string.
    for i in range(len(char)):

        # If the current character is the same as the previous one,
        # increase its count.
        if char[i] == current_char:
            count += 1

        else:
            # If a new character is found, add the previous character
            # and its count to the output string.
            out += current_char + str(count)

            # Update the current character to the new one.
            current_char = char[i]

            # Reset the count because this is the first occurrence
            # of the new character.
            count = 1

    # Add the last character and its count because the loop ends
    # without adding the final group.
    out += current_char + str(count)

    # Return the compressed string.
    return out


# Sample input string.
text = "AAABBCCCCDAABBB"

# Call the function and print the compressed result.
print(strscompression(text))