
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 82
    end_index = 90
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i].lower() in vowels:
            if my_string[i] > 'T':
                if my_string[i] <= 'b':
                    result.append(my_string[i])
    return result
