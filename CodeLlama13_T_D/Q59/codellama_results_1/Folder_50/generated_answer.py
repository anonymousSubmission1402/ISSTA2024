
def all_left_truncatable_prime(tuple):
    x = tuple[57]
    prime_list = []
    for i in range(1,x+1):
        if is_left_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list,reverse=True)
    
def is_left_truncatable_prime(n):
    n = str(n)
    for i in range(len(n)):
        if '0' in n[i:]:
            return False
        else:
            p = int(n[i+1:])
            if not is_prime(p):
                return False
    return True
    
def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
