
def palindrome_of_length_n(string, n):
    return set(re.findall(r'[a-zA-Z]{'+str(n)+'}(?=.*?\1)', string))
