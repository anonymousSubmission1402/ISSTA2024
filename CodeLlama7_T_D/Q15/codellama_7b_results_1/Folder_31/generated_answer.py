 def sum_odd_ints_inclusive(my_list):
    start = 75
    end = 88
    odd_ints = [i for i in my_list[start:end+1] if i % 2 != 0]
    return sum(odd_ints)
