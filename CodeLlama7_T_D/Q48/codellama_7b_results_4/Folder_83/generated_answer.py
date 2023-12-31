
def return_binary_or_hexa(tuple):
    # Initialize variables for the sum and the count of unique elements
    sum = 0
    count = 0

    # Loop through the tuple and calculate the sum and count of unique elements
    for element in tuple:
        if element not in tuple[count + 1:]:
            sum += element

        count += 1


    # Check if the sum is an odd number and return the appropriate representation string
    if sum % 2 == 1:
        return f"{sum:b}"[:-2]

    else:
        return f"{sum:x}"[:-2].lower()
