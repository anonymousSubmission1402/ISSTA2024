
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        for t in strings:
            if len(t) < 3:
                continue
            if s.lower() == t.lower():
                continue
            if ''.join(sorted(s)) == ''.join(sorted(t)):
                anagram_pairs += 1
    return anagram_pairs >= 21
