
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'(?i)(\w{85})', s) if p == p[::-1]}
