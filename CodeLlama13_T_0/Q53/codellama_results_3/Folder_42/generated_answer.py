
def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in re.findall(r'[a-zA-Z]{4,}', string) if len(palindrome) >= 44 and palindrome == palindrome[::-1]}
