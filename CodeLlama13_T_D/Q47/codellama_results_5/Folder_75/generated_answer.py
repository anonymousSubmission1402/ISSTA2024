
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31, 75):
        for j in range(23, 40):
            if string[i:i+j] == string[i+j-1:i-1:-1]:
                palindromes.add(string[i:i+j])
    return palindromes
