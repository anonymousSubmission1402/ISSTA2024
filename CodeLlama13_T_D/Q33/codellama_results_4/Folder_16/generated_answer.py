
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start, end = 133, 306
    return [c for c in s[start:end] if c.lower() in vowels and c <= 'd']
