
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(2, 7):
        if s[i] in vowels and s[i] <= 'd':
            result.append(s[i])
    return result
