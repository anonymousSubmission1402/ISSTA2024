
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(27, 58):
        if string[i].lower() in vowels and string[i] <= 'w':
            result.append(string[i])
    return result
