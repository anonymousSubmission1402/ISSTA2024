
def return_vowels(string):
    vowels = []
    for i in range(65, 70):
        if string[i-1].isalpha() and string[i-1].islower():
            if ord(string[i-1]) > ord("%") and ord(string[i-1]) <= ord("G"):
                vowels.append(string[i-1])
    return vowels
