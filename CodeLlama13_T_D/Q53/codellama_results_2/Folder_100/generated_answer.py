
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    return {p for p in re.findall('[a-z]{48,}', s) if p == p[::-1]}
