
def return_vowels(string):
    vowels = []
    for i in range(20, 43):
        if string[i].isupper() and string[i] in "AEIOU":
            vowels.append(string[i])
    return vowels
