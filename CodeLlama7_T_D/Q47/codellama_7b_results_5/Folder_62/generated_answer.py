 def palindromes_of_specific_lengths(string):
    # Find the substring between indices 26 and 87 (both inclusive)
    substring = string[26:87]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its opposite
        current_char = substring[i]
        opposite_char = substring[~i]
        # Check if the current character is a letter (a-zA-Z)
        if current_char.isalpha():
            # Check if the opposite character is also a letter (a-zA-Z)
            if opposite_char.isalpha():
                # Check if the current character and its opposite are the same letter
                if current_char.lower() == opposite_char.lower():
                    # Get the substring from the current character to the end of the string
                    sub_str = substring[i:]
                    # Check if there is a palindrome with length between 52 and 56 (both inclusive) in the substring
                    if len(sub_str) >= 52 and len(sub_str) <= 56:
                        # Split the substring into individual words
                        sub_words = sub_str.split()
                        for word in sub_words:
                            # Check if the word is a palindrome with length between 52 and 56 (both inclusive)
                            if len(word) >= 52 and len(word) <= 56:
                                # Add the word to the set of palindromes
                                palindromes.add(word)
    # Return the set of palindromes found in the substring
    return palindromes
