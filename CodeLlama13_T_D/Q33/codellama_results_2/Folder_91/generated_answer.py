
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(4, 8):
        if string[i].lower() in vowels and string[i] <= "r":
            result.append(string[i])
    return result
