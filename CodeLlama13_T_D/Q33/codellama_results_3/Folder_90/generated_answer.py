
def return_vowels(string):
    vowels = []
    for i in range(142, 145):
        if string[i].isalpha() and ord(string[i]) > 4 and ord(string[i]) <= ord('o'):
            vowels.append(string[i])
    return vowels
