
def palindromes_between_indices(s):
    indices = list(range(4, 9 + 1))
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in indices:
        for j in range(i - 6, i):
            if s[j] not in letters:
                continue
            for k in range(i + 1, i + 7):
                if k >= len(s) or s[k] not in letters:
                    break
                palindromes.add("".join(s[j:k]))
    return palindromes
