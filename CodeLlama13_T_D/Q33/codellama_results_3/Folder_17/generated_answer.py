
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(60, 99):
        if s[i].lower() in vowels and s[i] <= 'n' and s[i] >= 'j':
            result.append(s[i])
    return result
