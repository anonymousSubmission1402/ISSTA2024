
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the input list is empty

    if len(my_list) == 0:
        return None

    # Initialize variables to keep track of the smallest and second smallest elements

    smallest = float('inf')

    second_smallest = float('inf')

    # Iterate through the input list

    for i in range(len(my_list)):

        # Check if the current element is smaller than the smallest element so far

        if my_list[i] < smallest:

            # If it is, update the second smallest element and continue to the next element

            second_smallest = smallest

            smallest = my_list[i]

        # Check if the current element is smaller than the second smallest element so far

        elif my_list[i] < second_smallest:

            # If it is, update the second smallest element and continue to the next element

            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return None

    if second_smallest != float('inf'):

        return second_smallest


    else:

        return None
