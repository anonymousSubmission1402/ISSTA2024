
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams
    def is_anagram(string1, string2):
        # Convert the strings to lowercase
        string1 = string1.lower()
        string2 = string2.lower()
        # Sort the characters of each string
        sorted_string1 = "".join(sorted(string1))
        sorted_string2 = "".join(sorted(string2))
        # Check if the sorted strings are equal
        return sorted_string1 == sorted_string2
    # Define a variable to store the number of anagrams found
    num_anagrams = 0
    # Iterate over the list of strings and check for anagrams
    for string1 in my_list:
        for string2 in my_list:
            if is_anagram(string1, string2) and len(string1) >= 3:
                num_anagrams += 1
    # Return True if there are at most 70 pairs of anagrams in the given list
    return num_anagrams <= 70
