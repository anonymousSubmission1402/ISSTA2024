
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 2):
        substr = string[i:i+3]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
