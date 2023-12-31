
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each number in the range [1, x]
    for i in range(1, x+1):
        # Check if the current number is prime
        if is_prime(i):
            # Check if the current number contains no 0
            if '0' not in str(i):
                # Check if the current number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
                while len(str(i)) > 1:
                    i = int(str(i)[:-1])
                    if not is_prime(i):
                        break
                else:
                    result.append(i)
    
    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(result, reverse=True)
