
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-47):
        substring = string[i:i+48]
        if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
