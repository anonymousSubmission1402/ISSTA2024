
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 43
    end_index = 70
    filtered_list = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.lower() in vowels and char > '*' and char <= 'b':
            filtered_list.append(char)
    return filtered_list
