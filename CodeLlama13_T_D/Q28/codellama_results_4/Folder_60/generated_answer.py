
def return_nth_smallest_ascii(s):
    count = {}
    for i in range(36, 80):
        if s[i-1] not in count:
            count[s[i-1]] = 1
        else:
            count[s[i-1]] += 1
    
    smallest_ascii = sorted(count.items(), key=lambda x: x[1])[11][0]
    return smallest_ascii
