
def composite_nums_between_indices(num_list):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False
    
    return_set = {n for i, n in enumerate(num_list) if 80 <= i <= 200 and check_composite(n)}
    return return_set
