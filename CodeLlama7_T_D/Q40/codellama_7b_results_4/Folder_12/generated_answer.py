 def return_n_smallest_chars(s):
    # Sort the string in ascending order based on ASCII value
    s = sorted(s, key=ord)
    # Create a list of exactly 61 characters of the given string
    result = []
    for i in range(61):
        result.append(s[i])
    return result
