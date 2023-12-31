
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list)):
        # Compare each string with every other string using a case-insensitive comparison
        for j in range(i+1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_anagrams += 1
    # Return True if the number of anagrams is less than or equal to 15; otherwise return False
    return num_anagrams <= 15
