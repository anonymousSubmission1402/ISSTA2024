
def return_vowels(string):
    vowels = []
    for i in range(47, 89):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "@":
            vowels.append(string[i])
    return vowels
