import re
def all_substring_of_size_n(s):
    return re.findall(r"((?:[a-z]+\d){24})", s)
