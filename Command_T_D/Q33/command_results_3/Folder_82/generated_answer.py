import re
def return_vowels(str1):
    str1=re.sub(r'[^A-Z]', '', str1)
    str1=re.sub(r'[^\s]', '', str1)
    return list(str1[86:99])
