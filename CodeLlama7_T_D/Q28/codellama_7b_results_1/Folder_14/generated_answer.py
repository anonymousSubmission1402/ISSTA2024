
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between indices 46 and 82, both inclusive
    start_index = 46
    end_index = 82
    character_indices = []
    for i in range(start_index, end_index + 1):
        if string[i] not in character_indices:
            character_indices.append(string[i])
    
    # Sort the indices of the characters in ascending order based on their ASCII values

    sorted_character_indices = sorted(character_indices, key=lambda x: ord(x))

    # Return the character with the 16th smallest ASCII value among those characters

    return sorted_character_indices[15]
