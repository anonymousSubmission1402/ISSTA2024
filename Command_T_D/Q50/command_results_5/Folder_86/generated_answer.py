import re
def if_contains_anagrams(strs):
    return bool(re.findall(r'(?i)(?=.*[a-z])\1+', strs, flags=re.I))
