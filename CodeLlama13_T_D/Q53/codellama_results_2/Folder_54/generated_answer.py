
def palindrome_of_length_at_least_n(string):
    return {x for x in string if len(x) >= 74 and x == x[::-1]}
