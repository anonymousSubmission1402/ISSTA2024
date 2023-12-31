
def if_contains_anagrams(string_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings and check for anagrams
    for string in string_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a sorted version of the string
            sorted_string = "".join(sorted(lowercase_string))

            # Increment the count for this anagram
            if sorted_string in anagram_counts:
                anagram_counts[sorted_string] += 1

            else:
                anagram_counts[sorted_string] = 1

    # Check if there are at least 40 pairs of anagrams in the list
    return len(anagram_counts) >= 40
