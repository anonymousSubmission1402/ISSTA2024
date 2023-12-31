
def return_vowels(string):
    # Initialize an empty list to store the vowel characters
    vowels = []
    # Loop through each character in the string starting from index 60 and ending at index 99
    for i in range(60, 100):
        # Check if the current character is a vowel
        if string[i] in "aeiou":
            # Add the current character to the list of vowels
            vowels.append(string[i])
    # Return the list of vowel characters
    return vowels
