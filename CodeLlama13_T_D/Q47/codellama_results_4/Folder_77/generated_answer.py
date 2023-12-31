
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(103, 276+1):
        for j in range(i+99, i+170):
            if j-i < 100 or j-i > 169: continue
            substr = string[i:j]
            if len(substr) % 2 == 1: continue
            for k in range((len(substr)//2)+1):
                if substr[:k].lower() != substr[len(substr)-k:].lower(): break
            else: palindromes.add(substr)
    return palindromes
