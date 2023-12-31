
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 73):
        substr = string[i:i+74]
        
        if re.match(r'^[a-zA-Z]+$', substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
