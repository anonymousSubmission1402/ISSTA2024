
def gcf_three_nums(numbers):
    return _gcf_three_nums(numbers, 7, 6, 8)

def _gcf_three_nums(numbers, i1, i2, i3):
    return _gcf(numbers[i1], numbers[i2], numbers[i3])

def _gcf(a, b, c):
    if a == 0:
        return b
    g = _gcd(b, a)
    if c % g != 0:
        return 1
    return g

def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)
