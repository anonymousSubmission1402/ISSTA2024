
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            # Check if the two strings are anagrams
            if sorted(strings[i]) == sorted(strings[j]):
                # Increment the pair count
                pair_count += 1
    # Return true if there are at least 177 pairs of anagrams in the list
    return pair_count >= 177
