
def palindrome_of_length_n(s):
    return set((w,) for w in re.findall(r'[a-zA-Z]{19}', s))
