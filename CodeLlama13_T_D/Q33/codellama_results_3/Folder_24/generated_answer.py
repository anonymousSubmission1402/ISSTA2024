
def return_vowels(string):
    vowels = []
    for i in range(23, 57):
        if string[i].islower() and string[i] >= 'a' and string[i] <= 'd':
            vowels.append(string[i])
    return vowels
