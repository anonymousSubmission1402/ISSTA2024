
def palindrome_of_length_at_least_n(s):
    return {p for p in re.findall("[a-zA-Z]{133,}", s) if p == p[::-1]}
