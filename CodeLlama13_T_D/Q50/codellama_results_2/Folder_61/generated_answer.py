
def if_contains_anagrams(strings):
    anagram_pairs = set()
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3 and lower_string not in anagram_pairs:
            anagram_pairs.add(lower_string)
            for other_string in strings:
                if len(other_string) >= 3 and lower_string == other_string.lower():
                    anagram_pairs.add((lower_string, other_string))
    return len(anagram_pairs) >= 8
