
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if len(substring) == 42 and all(letter not in substring for letter in substring[1:]):
                substrings.append(substring)
    return substrings
