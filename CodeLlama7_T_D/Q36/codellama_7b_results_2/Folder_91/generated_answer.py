
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    for i in range(len(s)):

        if s[i] > '$' and s[i] < '?':
            continue

        else:

            new_str += s[i]

    return new_str
