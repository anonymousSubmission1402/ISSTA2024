
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 15 to index 86, both inclusive
    palindromes = []
    for i in range(15, 87):
        for j in range(i+1, min(len(string), 87)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    # Filter palindromes by length
    return {p for p in palindromes if len(p) in range(51, 61)}
