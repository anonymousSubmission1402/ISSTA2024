
def palindromes_between_indices(string):
    indices = range(1, 7+1)
    letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    palindromes = set()
    for i in indices:
        for j in indices:
            if j-i+1 < 7: continue
            substr = string[i-1:j]
            if len(substr) != j-i+1: continue
            if all(letter in letters for letter in substr):
                palindromes.add(substr)
    return palindromes
