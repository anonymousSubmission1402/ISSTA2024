
def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) < 3:
            continue
        anagram = "".join(sorted(string.lower()))
        if anagram not in anagrams:
            anagrams.append(anagram)
    return len(anagrams) >= 233
