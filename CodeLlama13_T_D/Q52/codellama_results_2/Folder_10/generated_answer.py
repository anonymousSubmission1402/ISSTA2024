
def palindrome_of_length_n(s):
    n = 54
    s = s.lower()
    return {p for p in (s[i:j+1] for i in range(len(s)) for j in range(i, len(s))) if p == p[::-1]}
