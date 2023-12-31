
def palindromes_of_specific_lengths(string):
    substr = string[26:84+1]
    lengths = range(30, 47)
    palindromes = set()
    for length in lengths:
        for i in range(len(substr)):
            if substr[i:i+length].lower() == substr[i:i+length][::-1].lower():
                palindromes.add(substr[i:i+length])
    return palindromes
