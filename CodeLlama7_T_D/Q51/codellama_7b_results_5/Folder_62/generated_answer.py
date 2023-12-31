
def if_contains_anagrams(words):
    # Create a set of all possible anagrams of the English alphabet
    anagram_set = set()
    for i in range(26):
        for j in range(i + 1, 26):
            for k in range(j + 1, 26):
                anagram_set.add((chr(97 + i), chr(97 + j), chr(97 + k))))
    # Iterate over the input list and check if each word is a anagram of any other word in the list
    for word1 in words:
        for word2 in words:
            if word1 == word2:
                continue

            if len(word1) < 3 or len(word2) < 3:
                continue

            if set(word1.lower()) == set(word2.lower()):
                return False

    # If no anagrams were found, return True

    return True
