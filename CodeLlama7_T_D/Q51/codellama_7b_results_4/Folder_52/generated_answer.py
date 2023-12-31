
def if_contains_anagrams(word_list):
    # Create a set to store the anagram pairs
    anagram_pairs = set()
    # Iterate over each word in the list
    for word in word_list:
        # Convert the word to lowercase
        word = word.lower()
        # Iterate over each letter in the word
        for letter in word:
            # If the letter is not a letter, continue to the next iteration
            if not letter.isalpha():
                continue

            # If the letter is already in the set of anagram pairs, continue to the next iteration
            if letter in anagram_pairs:
                continue

            # Create a new set to store the anagrams of the current letter
            anagrams = set()

            # Iterate over each word in the list
            for other_word in word_list:
                # If the current word is not the same as the other word, continue to the next iteration
                if word == other_word:
                    continue

                # Convert the other word to lowercase
                other_word = other_word.lower()
                # Check if the letter appears in the other word
                if letter in other_word:
                    # Add the anagram pair to the set of anagram pairs
                    anagram_pairs.add((letter, other_word[::-1])))

            # If there are at most 43 pairs of anagrams, return True
            if len(anagram_pairs) <= 43:
                return True

        # If there are more than 43 pairs of anagrams, return False
        return False
