
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(155, 284):
        for j in range(i+103, min(i+121, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
