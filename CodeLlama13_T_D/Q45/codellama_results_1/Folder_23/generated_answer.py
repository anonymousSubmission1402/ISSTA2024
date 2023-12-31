
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(0, len(string) - 6 + 1):
        for j in range(i + 4, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and all(letter in english_letters for letter in substring):
                palindromes.add(substring)
    return palindromes
