
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the prime number to the list
                prime_numbers.append(i)

    # Sort the list in ascending order
    prime_numbers.sort()

    # Return the list of all left-and-right-truncatable prime numbers less than or equal to x
    return prime_numbers

# Check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1
    return True

# Check if a number is a left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Initialize an empty string to store the number in string form
    num_str = ""

    # Convert the number to a string and store it in num_str
    num_str = str(n)

    # Check if the number is less than or equal to 1000
    if n <= 1000:
        # Initialize an empty list to store the prime factors of the number
        prime_factors = []

        # Find the prime factors of the number and store them in the list prime_factors
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Add the prime factor to the list
                prime_factors.append(i)

        # Initialize an empty string to store the number in string form without any leading leftmost or last rightmost digits
        num_str_wo_leading = ""

        # Initialize an empty string to store the number in string form without any trailing rightmost digits
        num_str_wo_trailing = ""

        # Extract the first digit from the number in string form and store it in a variable called first_digit
        first_digit = num_str[0]

        # Extract the last digit from the number in string form and store it in a variable called last_digit
        last_digit = num_str[-1]

        # Check if the first digit is equal to 0 or the last digit is equal to 0
        if first_digit == "0" or last_digit == "0":
            # Return False if either of the conditions are met
            return False

        # Remove the leading leftmost and last rightmost digits from the number in string form and store it in num_str_wo_leading and num_str_wo_trailing respectively
        num_str_wo_leading = num_str[1:]
        num_str_wo_trailing = num_str[:-1]

        # Check if the number is a prime number after removing its leading leftmost and last rightmost digits
        if is_prime(int(num_str_wo_leading))) == True or is_prime(int(num_str_wo_trailing))) == True:
            # Return False if either of the conditions are met
            return False

        # Check if all the prime factors of the number are present in num_str_wo_leading and num_str_wo_trailing respectively
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Initialize an empty string to store the first digit of the number divided by the prime factor in string form
                first_digit_divided = ""

                # Initialize an empty string to store the last digit of the number divided by the prime factor in string form
                last_digit_divided = ""

                # Extract the first digit from the number in string form divided by the prime factor and store it in a variable called first_digit_divided
                first_digit_divided = str(n // i)[0]

                # Extract the last digit from the number in string form divided by the prime factor and store it in a variable called last_digit_divided
                last_digit_divided = str(n // i)[-1]

                # Check if the first digit of the number is equal to the first digit of the number divided by the prime factor and the last digit of the number is equal to the last digit of the number divided by the prime factor
                if (first_digit == first_digit_divided) and (last_digit == last_digit_divided)):
                    # Remove the leading leftmost and last rightmost digits from the number in string form divided by the prime factor and store it in num_str_wo_leading and num_str_wo_trailing respectively
                    num_str_wo_leading = str(n // i)[1:]
                    num_str_wo_trailing = str(n // i)[:-1]

                    # Check if the number is a prime number after removing its leading leftmost and last rightmost digits
                    if is_prime(int(num_str_wo_leading))) == True or is_prime(int(num_str_wo_trailing))) == True:
                        # Return False if either of the conditions are met
                        return False

                # Check if the first digit of the number divided by the prime factor is equal to 0 or the last digit of the number divided by the prime factor is equal to 0
                if (first_digit_divided == "0") or (last_digit_divided == "0")):
                    # Return False if either of the conditions are met
                    return False

        # Check if the number is a palindrome after removing its leading leftmost and last rightmost digits
        if is_palindrome(int(num_str_wo_leading))) == True or is_palindrome(int(num_str_wo_trailing)))):
            # Return False if either of the conditions are met
            return False

        # Check if the number is a palindrome after removing its leading leftmost and last rightmost digits without considering the first and last digit of the number
        elif num_str_wo_leading == str(num)[1:-1]) or (num_str_wo_trailing == str(num)[:-1])):
            # Return False if either of the conditions are met
            return False

    # Check if the number is a prime number after removing its leading leftmost and last rightmost digits without considering the first digit of the number or the last digit of the number
    elif (num_str_wo_leading == str(num)[1:])) or (num_str_wo_trailing == str(num)[:-1])):
        # Check if all the prime factors of the number are present in num_str_wo_leading and num_str_wo_trailing respectively
        for i in range(2, int(n ** 0.5) + 1)):
            # Check if i divides n
            if n % i == 0:
                # Initialize an empty string to store the first digit of the number divided by the prime factor in string form
                first_digit_divided = ""

                # Initialize an empty string to store the last digit of the number divided by the prime factor in string form
                last_digit_divided = ""

                # Extract the first digit from the number in string form divided by the prime factor and store it in a variable called first_digit_divided
                first_digit_divided = str(n // i)[0]

                # Extract the last digit from the number in string form divided by the prime factor and store it in a variable called last_digit_divided
                last_digit_divided = str(n // i)[-1]

                # Check if the first digit of the number is equal to the first digit of the number divided by the prime factor and the last digit of the number is equal to the last digit of the number divided by the prime factor
                if (first_digit_divided != num_str_wo_leading[0] or last_digit_divided != num_str_wo_trailing[-1])):
                    # Return False if either of the conditions are met
                    return False

        # Check if the number is a palindrome after removing its leading leftmost and last rightmost digits without considering the first digit of the number or the last digit of the number
        if is_palindrome(int(num_str_wo_leading))) == True or is_palindrome(int(num_str_wo_trailing)))):
            # Return False if either of the conditions are met
            return False

    # If none of the above conditions are met, return True
    else:
        return True
