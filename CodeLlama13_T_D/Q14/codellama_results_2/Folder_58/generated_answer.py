
def find_second_smallest_num(distinct_numbers):
    second_smallest = None
    for i in range(310, 371):
        if distinct_numbers[i] < second_smallest or second_smallest is None:
            second_smallest = distinct_numbers[i]
    return second_smallest
