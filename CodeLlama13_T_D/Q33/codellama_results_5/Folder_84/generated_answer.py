
def return_vowels(string):
    vowels = []
    for i in range(770, 852):
        if string[i].isalpha() and string[i].lower() not in "aeiou" and ord(string[i]) > ord("b") and ord(string[i]) <= ord("i"):
            vowels.append(string[i])
    return vowels
