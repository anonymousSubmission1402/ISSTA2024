
def if_perfect_num(numbers):
    return numbers[43] in perfect_numbers(numbers)

def perfect_numbers(numbers):
    perfect = []
    for n in numbers:
        root = int(n**0.5)
        if root**2 == n and all(i+1 not in perfect for i in range(root)):
            perfect.append(n)
    return perfect
