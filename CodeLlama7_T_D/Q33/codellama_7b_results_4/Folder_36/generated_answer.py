 def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and if it is between index 604 (inclusive) and index 949 (exclusive)
        if char.isalpha() and 604 <= my_string.index(char) < 949:
            # If the condition is true, add the character to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
