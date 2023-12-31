
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(106, 281):
        for j in range(i+135, i+152):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
