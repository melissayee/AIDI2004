def math_operations(num1, num2):
    valid_input = False
    while valid_input == False:
        function = input("Which math operation would you like to perform? (+, -, *, /) ")
        if function not in ['+', '-', '*', '/']:
            print ("You did not select a valid operation, please try again")
        elif function == '+':
            result = num1 + num2
            valid_input = True
        elif function == '-':
            result = num1 - num2
            valid_input = True
        elif function == '*':
            result = num1 * num2
            valid_input = True
        else:
            if num2 == 0:
                print ("You cannot divide by 0, please select another operation")
                continue
            else:
                result = num1/num2
                valid_input = True
    return round(result,2)
