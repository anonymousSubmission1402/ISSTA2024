
def palindromes_of_specific_lengths(string):
    # Find all palindromes of the given length in the substring
    palindromes = {p for p in re.findall(r'(.*?){5,10}', string[100:200]) if p == p[::-1]}
    return palindromes
