
def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        lowercase_string = string.lower()
        anagrams = []
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if lowercase_string.count(letter) > 1:
                anagram = ""
                for char in lowercase_string:
                    if char == letter:
                        anagram += char
                anagrams.append(anagram)
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count <= 147
