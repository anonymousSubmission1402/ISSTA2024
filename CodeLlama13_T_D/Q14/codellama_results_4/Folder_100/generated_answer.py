
def find_second_smallest_num(my_list):
    if len(my_list) < 52:
        return None
    
    second_smallest = float('inf')
    for i in range(43, 52):
        num = my_list[i]
        if num < second_smallest:
            second_smallest = num
            
    return second_smallest
