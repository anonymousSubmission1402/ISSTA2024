
def return_vowels(string):
    vowels = []
    for i in range(20, 34):
        if string[i].islower() and 'a' <= string[i] <= 'i':
            vowels.append(string[i])
    return vowels
