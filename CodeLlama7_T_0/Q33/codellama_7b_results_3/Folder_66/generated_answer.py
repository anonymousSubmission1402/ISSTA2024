
def return_vowels(my_string):
    vowels = []
    for i in range(63, 79):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            if my_string[i] > 'D' and my_string[i] <= 'y':
                vowels.append(my_string[i])
    return vowels
