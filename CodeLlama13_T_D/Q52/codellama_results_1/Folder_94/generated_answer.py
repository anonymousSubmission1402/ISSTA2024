
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        if string[i:i+93].lower() == string[i:i+93][::-1]:
            palindromes.add(string[i:i+93])
    return palindromes
