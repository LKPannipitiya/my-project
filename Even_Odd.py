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

# Test the function with different numbers
print(is_even(4))  # Expected output: 'Even'
print(is_even(7))  # Expected output: 'Odd'
