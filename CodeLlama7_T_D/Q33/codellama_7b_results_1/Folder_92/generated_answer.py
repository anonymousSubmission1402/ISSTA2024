
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 3
    end_index = 8
    filtered_vowels = []
    for vowel in vowels:
        if vowel > ';' and vowel <= 'D':
            filtered_vowels.append(vowel)
    return filtered_vowels[start_index:end_index]
