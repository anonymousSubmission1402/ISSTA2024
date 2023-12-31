
def palindromes_between_indices(s):
    indices = range(0, 4)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = []
    for i in indices:
        for j in indices:
            if i <= j:
                substr = s[i:j+1]
                if len(substr) >= 3 and all(l in letters for l in substr):
                    palindromes.append("".join(reversed(substr)))
    return set(palindromes)
