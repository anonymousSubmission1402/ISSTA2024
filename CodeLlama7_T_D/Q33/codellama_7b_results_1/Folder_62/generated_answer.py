
def return_vowels(string):
    vowels = ["A", "E", "I", "O", "U"]
    start_index = 14
    end_index = 60
    filtered_vowels = []
    for i in range(start_index, end_index):
        if string[i] in vowels and string[i].lower() > "d" and string[i].lower() <= "v":
            filtered_vowels.append(string[i])
    return filtered_vowels
