
def return_vowels(my_string):
    # Define a list to store the vowel characters
    vowels = []
    # Iterate over the characters in the string
    for char in my_string:
        # Check if the character is a vowel and meets the specified criteria
        if char.isalpha() and char.lower() in "aeiou" and ord(char) > 22 and ord(char) <= 82:
            # If it does, add it to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
