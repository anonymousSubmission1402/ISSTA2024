
def palindrome_of_length_n(string):
    n = 60
    palindromes = set()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    
    return palindromes
