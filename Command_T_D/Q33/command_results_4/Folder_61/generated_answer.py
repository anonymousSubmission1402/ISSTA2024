import re
def return_vowels(s):
    return re.findall(r'[A-E][^C-I]', s)
