import re
def remove_repeat_chars(s):
    return re.sub(r'(.)\1(.)\2(.)\3(.)\4(.)\5(.)\6(.)\7(.)\8', r'\1\2\3\4\5\6\7\8', s)
