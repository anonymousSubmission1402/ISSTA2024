
def palindromes_of_specific_lengths(string):
    substring = string[10:97]
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i+length-1::-1]:
                palindromes.add(substring[i:i+length])
    return palindromes
