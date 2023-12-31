
def if_contains_anagrams(words):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in words:
        # Convert the word to lowercase
        word = word.lower()

        # Check if the word is at least three characters long
        if len(word) < 3:
            continue

        # Get a list of all the letters in the word
        letters = [letter for letter in word]

        # Sort the list of letters
        sorted_letters = sorted(letters)

        # Join the sorted letters back into a string
        anagram = "".join(sorted_letters)

        # Increment the count for this anagram
        if anagram in anagram_counts:
            anagram_counts[anagram] += 1
        else:
            anagram_counts[anagram] = 1

    # Check if there are at most 116 pairs of anagrams in the given list
    return len(anagram_counts) <= 116
