
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    index_4 = string[3]
    index_8 = string[7]
    if index_4 not in vowels or index_8 not in vowels:
        return []
    else:
        return [char for char in string[3:8] if char in vowels and char >= "p" and char <= "r"]
