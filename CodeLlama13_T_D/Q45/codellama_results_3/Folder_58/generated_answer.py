
def palindromes_between_indices(s):
    return {f"{s[i:j]}".lower() for i in range(len(s)-5) for j in range(i+6, len(s)+1) if f"{s[i:j]}".lower() == f"{s[j-1:i-1:-1]}".lower()}
