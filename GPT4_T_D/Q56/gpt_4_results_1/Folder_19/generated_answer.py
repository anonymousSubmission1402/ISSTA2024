
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 17):
        substring = string[i:i+18]
        if len(set(substring)) == 18:
            substrings.append(substring)
    return list(set(substrings))
