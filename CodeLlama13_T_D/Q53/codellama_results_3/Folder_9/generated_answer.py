
def palindrome_of_length_at_least_n(s):
    return {word for word in s if len(word) >= 95 and word == word[::-1]}
