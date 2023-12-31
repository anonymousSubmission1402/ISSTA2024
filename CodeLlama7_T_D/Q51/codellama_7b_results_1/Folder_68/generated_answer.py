
def if_contains_anagrams(word_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False

    # Iterate over the list of words and count the number of anagrams
    for word1 in word_list:
        for word2 in word_list:
            if word1 != word2 and len(word1) >= 3 and len(word2) >= 3:
                # Check if the two words are anagrams
                if sorted(word1) == sorted(word2):
                    anagram_count += 1
                    if anagram_count > 94:
                        return False

    return True
