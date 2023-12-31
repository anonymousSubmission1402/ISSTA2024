
def return_n_greatest_chars(input_string):
    # Initialize an empty list to store the sorted characters
    sorted_characters = []

    # Iterate through each character in the input string
    for character in input_string:

        # Add the current character to the sorted list if it has not been added yet
        if character not in sorted_characters:
            sorted_characters.append(character)

        # Sort the sorted list in descending order based on the ASCII values of each character
        sorted_characters.sort(key=ord, reverse=True)

        # If the length of the sorted list is greater than 35, remove the first element from the list
        if len(sorted_characters) > 35:
            sorted_characters.pop(0)

    # Return the sorted list of exactly 35 characters with the greatest ASCII values
    return sorted_characters[:35]
