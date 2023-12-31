
def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for string in list_of_strings:
        string_lower = string.lower()
        for i in range(len(string_lower) - 2):
            substring = string_lower[i:i+3]
            if substring != 'the' and substring in string_lower[i+1:]:
                anagram_count += 1
    return anagram_count <= 277
