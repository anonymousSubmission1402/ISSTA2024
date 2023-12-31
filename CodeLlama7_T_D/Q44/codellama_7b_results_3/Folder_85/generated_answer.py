
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list and check if each number is composite between indices 3 and 5
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(3, 6):
                if (my_list[i] % my_list[j]) == 0:
                    composite_nums.add(my_list[i])
                    break

    # Return the set of all composite numbers between indices 3 and 5
    return composite_nums
