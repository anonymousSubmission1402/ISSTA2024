
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(5, 10):
        for j in range(i + 1, len(string)):
            if string[i:j].isalpha():
                palindromes.add(string[i:j])
    return palindromes
