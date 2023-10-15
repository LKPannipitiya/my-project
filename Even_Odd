def is_even(number):
    """
    Check if a number is even or odd.

    Args:
    number (int): The number to check.

    Returns:
    str: 'Even' if the number is even, 'Odd' if it's odd.
    """
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
def is_prime(number):
    """
    Check if a number is prime.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test the function with different numbers
print(is_even(4))  # Expected output: 'Even'
print(is_even(7))  # Expected output: 'Odd'
print("is_prime(11):", is_prime(11))  # Expected output: True
print("is_prime(4):", is_prime(4))  # Expected output: False