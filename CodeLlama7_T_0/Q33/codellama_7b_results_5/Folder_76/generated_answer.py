
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 495
    end_index = 837
    result = []
    for i in range(start_index, end_index + 1):
        if my_string[i].isalpha() and my_string[i].lower() in vowels and my_string[i] > 'B' and my_string[i] <= 't':
            result.append(my_string[i])
    return result
