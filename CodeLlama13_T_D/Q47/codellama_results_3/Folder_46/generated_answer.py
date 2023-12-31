
def palindromes_of_specific_lengths(string):
    lengths = range(29, 63)
    indices = range(11, 98)
    palindromes = set()
    for length in lengths:
        for i in indices:
            substring = string[i : i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
