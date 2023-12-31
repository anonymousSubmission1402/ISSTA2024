
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8]
    palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in permutations(s, i):
            perm = ''.join(perm).lower()
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes
