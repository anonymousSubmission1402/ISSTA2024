
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if not any(substring[j] == substring[j-1] for j in range(1, len(substring))):
            substrings.append(substring)
    return substrings
