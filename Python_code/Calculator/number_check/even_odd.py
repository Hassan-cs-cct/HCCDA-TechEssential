def even_odd(number):
    """
    Check if a number is even or odd.
    
    Args:
    number (int): The number to check.
    
    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"