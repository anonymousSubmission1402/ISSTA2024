
def palindrome_of_length_at_least_n(string):
    return {word for word in string if len(word) >= 63 and word == word[::-1]}
