
def palindromes_of_specific_lengths(string):
    substr = string[0:100]
    palindromes = set()
    for i in range(3, 16):
        for j in range(len(substr) - i + 1):
            if substr[j:j+i].lower() == substr[j+i-1:j-1:-1]:
                palindromes.add(substr[j:j+i])
    return palindromes
