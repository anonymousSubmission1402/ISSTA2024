
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(528, 606):
        if s[i].isalpha() and s[i] not in vowels:
            continue
        result.append(s[i])
    return result
