
def return_vowels(my_string):
    vowels = []
    for i in range(17, 65):
        if my_string[i].isalpha() and my_string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            if my_string[i] > 'U' and my_string[i] <= '{':
                vowels.append(my_string[i])
    return vowels
