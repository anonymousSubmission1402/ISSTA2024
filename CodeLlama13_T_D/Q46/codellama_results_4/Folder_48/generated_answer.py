
def gcf_three_nums(numbers):
    gcf = 1
    for i in range(654, 700):
        gcf = max(gcf, numbers[i])
    return gcf
