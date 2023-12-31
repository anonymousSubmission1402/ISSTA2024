
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(100, 300+1):
        for j in range(i, min(len(string), i+100)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
