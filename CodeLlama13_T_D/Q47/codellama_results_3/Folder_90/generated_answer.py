
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(106, 280+1):
        for j in range(i+136-1, i+151+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
