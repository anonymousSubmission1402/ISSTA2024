
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if string[i] >= "!" and string[i] <= "A":
            result += string[i]
    return result
