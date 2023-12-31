
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    
    # Iterate over each element in the tuple
    for element in tuple:
        
        # Check if the element is a prime number
        if is_prime(element):
            
            # If it is, add it to the list of prime numbers
            prime_numbers.append(element)
            
            # Now iterate over each digit in the element, starting from the leftmost digit
            for i in range(len(str(element)))):
                
                # Check if the current digit is 0
                if str(element)[i] == "0":
                    
                    # If it is, break out of the loop and move on to the next element
                    break
                
                # Otherwise, check if removing the current leftmost digit results in a prime number
                elif is_prime(int(str(element))[1:])):
                    
                    # If it does, add the resulting prime number to the list of prime numbers
                    prime_numbers.append(int(str(element))[1:]))
                    
                    # Now break out of the loop and move on to the next element
                    break
                
                # Otherwise, continue iterating over each digit in the current element
                else:
                    
                    continue
        
        # If the element is not a prime number, skip it and move on to the next element
        else:
            
            continue
    
    
    # Return the list of all left-truncatable prime numbers less than x in ascending order
    return sorted(prime_numbers)
