
def palindrome_of_length_at_least_n(string, n):
    return {x for x in re.findall(r'[a-zA-Z]{%s}' % n, string) if x == x[::-1]}
