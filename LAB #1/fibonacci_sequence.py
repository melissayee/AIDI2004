"""
Function Description: A function that will return the fibonacci sequence up to the nth number
Inputs: n (int)
Outputs: sequence (list)

Examples:
fibonacci(5) -> [0, 1, 1, 2, 3]
fibonacci(1) -> [0]
fibonacci(-1) -> "Invalid Input"
"""


def fibonacci(n):
    sequence = [0, 1]
    num1 = sequence[0]
    num2 = sequence[1]
    if n <= 0:
        sequence = "Invalid Input"
    elif n == 1:
        sequence = [0]
    else:
        for i in range(n-2):
            add = num1 + num2
            sequence.append(add)
            num1 = num2
            num2 = add
    return sequence
