
def palindromes_between_indices(s):
    indices = range(3, 9+1)
    return {p for p in set("".join(permutations(s[i:j]))) if len(p) >= 3 and p == p[::-1]}
