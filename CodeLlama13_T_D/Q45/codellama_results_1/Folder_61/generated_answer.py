
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(len(string) - 7 + 1):
        substr = string[i:i+7]
        if len(substr) < 7:
            continue
        for j in range(len(substr)):
            rev_substr = substr[:j+1][::-1]
            if rev_substr == substr[:j+1]:
                palindromes.add(rev_substr)
    return palindromes
