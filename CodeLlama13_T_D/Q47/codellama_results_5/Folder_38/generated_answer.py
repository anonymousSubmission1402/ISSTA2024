
def palindromes_of_specific_lengths(string):
    # find all palindromes in the given string
    palindromes = []
    for i in range(18, 88):
        for j in range(i+37, i+61):
            if string[i:j] == string[j-1:i-1:-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
