
def insert_after_character(string):
    # Iterate through the string and check for the occurrence of character '0'
    for i in range(len(string)):
        if string[i] == '0':
            # If an occurrence is found, insert the character 'H' immediately after it
            string = string[:i+1] + 'H' + string[i+1:]
    return string
