
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(125, 284):
        for j in range(i+9, i+127):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
