
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(2, len(string)):
        for j in range(i+1, len(string)+1):
            substr = string[i:j]
            if len(substr) >= 3 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    return palindromes
