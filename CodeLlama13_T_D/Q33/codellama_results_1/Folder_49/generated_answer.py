
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[10:97] if char in vowels and ord(char) > ord('r')]
