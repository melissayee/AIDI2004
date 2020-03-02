"""
Function Description: A function that determines whether a number is prime or not
Inputs: n (int)
Outputs: result (bool)

Examples:
prime(2) -> False
prime(1) -> False
prime(23) -> True
"""


def prime(n):
    result = True
    if n < 3:
        result = False
    else:
        for i in range(2, n):
            if n % i == 0:
                result = False
                break
    return result
