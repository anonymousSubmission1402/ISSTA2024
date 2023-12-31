
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in set(re.findall(r'\b[A-Za-z]{96,}\b', string, re.IGNORECASE)) if len(palindrome) >= 96 and palindrome == palindrome[::-1]}
