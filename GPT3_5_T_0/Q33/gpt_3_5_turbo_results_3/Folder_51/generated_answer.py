
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 68):
        if string[i] in vowels and 'M' < string[i] <= 'X':
            result.append(string[i])
    return result
