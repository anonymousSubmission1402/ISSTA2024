
def return_vowels(s):
    vowels = []
    for i in range(47, 89):
        if s[i].isalpha() and s[i] not in "aeiouAEIOU@n":
            vowels.append(s[i])
    return vowels
