
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 23
    end_index = 38
    subset = my_string[start_index:end_index]
    filtered_subset = [char for char in subset if char in vowels]
    return filtered_subset
