 def filter_chars(s):
    start = 73
    end = 74
    result = ""

    for char in s:
        if char == "U" or char <= "l":
            continue

        result += char

    return result
