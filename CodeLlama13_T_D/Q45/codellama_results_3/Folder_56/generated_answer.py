
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(5, 10):
        for j in range(i+1, 11):
            substring = string[i:j]
            if len(substring) >= 5 and all(letter in english_letters for letter in substring.lower()):
                palindromes.add(substring)
    return palindromes
