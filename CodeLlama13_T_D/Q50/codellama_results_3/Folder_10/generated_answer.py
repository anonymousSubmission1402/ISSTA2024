
def if_contains_anagrams(string_list):
    return len([s for s in string_list if len(set(s)) >= 3 and len(set(sorted(s))) < len(s)]) > 52
