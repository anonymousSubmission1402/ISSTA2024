
def palindrome_of_length_at_least_n(string, n):
    return {word for word in string if len(word) >= n and word == word[::-1]}
