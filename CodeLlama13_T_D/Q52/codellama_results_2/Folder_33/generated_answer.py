
def palindrome_of_length_n(string, n):
    return set((s[::-1]) for s in (re.findall('(?i)[a-zA-Z]{475}', string)))
