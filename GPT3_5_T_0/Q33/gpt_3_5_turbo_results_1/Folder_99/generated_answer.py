
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(323, 526):
        if string[i] in vowels and ord(string[i]) > ord('+') and ord(string[i]) <= ord(':'):
            result.append(string[i])
    return result
