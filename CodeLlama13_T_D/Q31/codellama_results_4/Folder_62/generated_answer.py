
def if_perfect_num(my_list):
    index = 926
    return my_list[index] in get_perfect_numbers(my_list)

def get_perfect_numbers(my_list):
    perfect_numbers = []
    for i, num in enumerate(my_list):
        divisors = [d for d in range(1, int(num**0.5)+1) if num % d == 0]
        if sum(divisors[1:]) == num:
            perfect_numbers.append(num)
    return perfect_numbers
