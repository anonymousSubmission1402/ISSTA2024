
def palindrome_of_length_n(string):
    return {palindrome for i in range(len(string) - 60 + 1) if string[i:i+60] == string[i+60:i:-1]}
