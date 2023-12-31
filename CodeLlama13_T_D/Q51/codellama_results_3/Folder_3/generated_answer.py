
def if_contains_anagrams(mylist):
    anagrams = []
    for word in mylist:
        lowercase = word.lower()
        sorted_word = "".join(sorted(lowercase))
        if sorted_word not in anagrams:
            anagrams.append(sorted_word)

    pairs = 0
    for i, word1 in enumerate(anagrams):
        for j, word2 in enumerate(anagrams[i+1:]):
            if len(word1) >= 3 and len(word2) >= 3:
                if "".join(sorted(word1)) == "".join(sorted(word2)):
                    pairs += 1

    return pairs <= 66
