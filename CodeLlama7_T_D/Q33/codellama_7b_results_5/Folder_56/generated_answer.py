
def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for char in my_string[15:86]:
        if char in vowels and char > "@":
            result.append(char)

    return result
