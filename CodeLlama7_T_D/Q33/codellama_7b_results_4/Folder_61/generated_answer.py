
def return_vowels(my_string):
    # Create a list of all vowel English letters in the given string
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    # Initialize an empty list to store the desired characters
    desired_chars = []
    # Iterate through the characters in the given string
    for char in my_string:
        # Check if the current character is a vowel and is greater than character C and smaller than or equal to character I
        if char.lower() in vowel_list and ord(char) > ord('C') and ord(char) <= ord('I'):
            # Add the current character to the list of desired characters
            desired_chars.append(char)
    # Return the list of desired characters
    return desired_chars
