
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in strings:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a sorted version of the string
            sorted_string = "".join(sorted(lowercase_string))

            # Increment the count for this anagram
            anagram_counts[sorted_string] = anagram_counts.get(sorted_string, 0) + 1

    # Check if there are at least 25 pairs of anagrams in the list
    return len(anagram_counts) >= 25
