
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 97):
        if string[i] in vowels and string[i] > 'R' and string[i] <= 'b':
            result.append(string[i])
    return result
