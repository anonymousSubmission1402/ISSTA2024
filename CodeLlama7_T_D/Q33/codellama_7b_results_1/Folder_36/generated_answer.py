 def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 604
    end_index = 949
    result = []
    for i in range(start_index, end_index):
        if my_string[i].isalpha() and my_string[i] in vowels and my_string[i].lower() > 'n' and my_string[i].lower() <= 'u':
            result.append(my_string[i])
    return result
