
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the 11th smallest number from index 20 to index 200, both inclusive
    nth_index = (len(my_list) // 5) * 4 + 10
    # Return the 11th smallest number
    return my_list[nth_index]
