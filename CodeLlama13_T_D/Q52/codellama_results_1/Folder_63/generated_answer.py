
def palindrome_of_length_n(s):
    return {p for p in {s[i:j] for i in range(len(s) - 17) for j in range(i + 18, len(s) + 1)} if all(c.isalpha() and c.lower() == c for c in p)}
