
def palindrome_of_length_n(s):
    return set([word for word in s.lower().split() if len(word) == 10 and word[::-1] == word])
