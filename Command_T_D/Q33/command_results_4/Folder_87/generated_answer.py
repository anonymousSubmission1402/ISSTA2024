import re
def return_vowels(s):
    return re.findall(r'[A-E-I-O]', s)[-3:]
