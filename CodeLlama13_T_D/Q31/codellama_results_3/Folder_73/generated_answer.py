
def if_perfect_num(numbers):
    for i in range(len(numbers)):
        if numbers[i] == 41:
            is_perfect = True
            for j in range(2, int(numbers[i]/2) + 1):
                if numbers[i] % j == 0 and j**2 != numbers[i]:
                    is_perfect = False
                    break
            return is_perfect
    return False
