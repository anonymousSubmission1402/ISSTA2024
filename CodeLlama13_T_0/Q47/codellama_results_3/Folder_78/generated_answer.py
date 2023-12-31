
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(15, 73):
        for j in range(i+19, min(len(string), i+56)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
