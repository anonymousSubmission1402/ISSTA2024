
def return_nth_smallest_ascii(s):
    count = {}
    for i in range(25, 64+1):
        if s[i-1] not in count:
            count[s[i-1]] = 0
        count[s[i-1]] += 1
    
    nth_smallest = None
    for i in range(25, 64+1):
        if count[s[i-1]] == 6:
            nth_smallest = s[i-1]
            break
        
    return nth_smallest
