
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    indices = range(23, 38)
    result = []
    for i in indices:
        if string[i] in vowels and string[i] > "n" and string[i] <= "k":
            result.append(string[i])
    return result
