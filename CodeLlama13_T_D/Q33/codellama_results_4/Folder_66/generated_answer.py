
def return_vowels(string):
    vowels = []
    for i in range(63, 79):
        if string[i].isalpha() and string[i].lower() >= "d" and string[i].lower() <= "y":
            vowels.append(string[i])
    return vowels
