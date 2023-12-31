
def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        length = len(string)
        if length >= 3:
            anagram_count += count_anagrams(string)
    return anagram_count <= 49

def count_anagrams(string):
    anagram_count = 0
    for i in range(len(string)):
        if string[i] in 'abcdefghijklmnopqrstuvwxyz':
            anagram_count += 1
    return anagram_count
