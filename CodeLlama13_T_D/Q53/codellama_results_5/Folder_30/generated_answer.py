
def palindrome_of_length_at_least_n(s):
    return {p for p in set(re.findall(r'(?i)(.)\1+', s)) if len(p) >= 16}
