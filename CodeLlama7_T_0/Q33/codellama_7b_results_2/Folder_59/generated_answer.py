
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 8
    end_index = 9
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] in vowels and my_string[i] > 'Y' and my_string[i] <= 's':
            result.append(my_string[i])
    return result
