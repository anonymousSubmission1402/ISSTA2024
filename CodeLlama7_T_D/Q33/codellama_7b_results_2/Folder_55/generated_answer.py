 def return_vowels(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for char in my_string[1:5]:
        if char.isalpha() and char.lower() in vowels and char > "!" and char <= "j":
            result.append(char)
    return result
