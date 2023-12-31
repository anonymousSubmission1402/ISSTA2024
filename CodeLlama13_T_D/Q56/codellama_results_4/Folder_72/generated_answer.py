
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 88 + 1):
        substring = string[i:i+88]
        if len(set(substring)) == 88 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
