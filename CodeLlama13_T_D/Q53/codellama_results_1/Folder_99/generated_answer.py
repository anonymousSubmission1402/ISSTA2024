
def palindrome_of_length_at_least_n(string):
    return {word for word in string if word == word[::-1] and len(word) >= 115}
