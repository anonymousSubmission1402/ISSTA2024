
def palindrome_of_length_at_least_n(string):
    return {pal for pal in string.lower() if len(pal) >= 96 and pal == pal[::-1]}
