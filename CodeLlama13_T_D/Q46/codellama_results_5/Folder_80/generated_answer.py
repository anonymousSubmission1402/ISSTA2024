
def gcf_three_nums(numbers):
    indices = [13, 76, 44]
    gcf = numbers[indices[0]]
    for i in range(1, len(indices)):
        gcf = gcf_two_nums(gcf, numbers[indices[i]])
    return gcf
