
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    n = 80
    palindromes = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
