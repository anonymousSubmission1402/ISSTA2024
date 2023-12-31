
def return_binary_or_hexa(t):
    a = t[18]
    b = t[52]
    total = 0
    
    for i in range(a + 1, b):
        if i not in t[18:52]:
            total += i
    
    if total == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
