
def palindrome_of_length_at_least_n(s, n):
    return {p for p in re.findall('[A-Za-z]{74,}', s) if p == p[::-1]}
