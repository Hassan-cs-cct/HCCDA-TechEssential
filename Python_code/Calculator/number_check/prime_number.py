def prime_number(n):
    """Check if a number is prime."""
    if n <= 1:
        return False

    i = 2
    flag = True

    while i < n:
        if n % i == 0:
            flag = False
            break
        i += 1

    if flag:
        print("Entered number is a prime number")
    else:
        print("Entered number is not a prime number")