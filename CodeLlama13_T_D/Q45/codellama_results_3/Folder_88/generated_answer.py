
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(3, 8):
        for j in range(i, len(string) - i + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
