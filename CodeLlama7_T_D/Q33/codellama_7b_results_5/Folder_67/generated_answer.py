
def return_vowels(my_string):
    vowels = []
    for i in range(21, 59):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            if my_string[i] > '/' and my_string[i] <= 'a':
                vowels.append(my_string[i])
    return vowels
