def calculator():
    # Here user needs to choose which operation
    # 1 is for addition 2 is for substraction 3 is for multiplication 4 is for division
    print('Which operation would you like to do?')
    print('1. Addition   2. Substraction   3. Multiplication   4. Division')
    choice = input('')
    # .upper method is used for possible crashes. Whatever user will enter
    # unless it is different than the characters of 'addition' will automatically converted to 'ADDITION'
    # this method is also applied to other operations
    if choice == "1" or choice.upper == "ADDITION":
        print('Please enter the numbers you would like to add')
        number1 = input('Number 1: ')
        number2 = input('Number 2: ')
        number_sum = int(number1) + int(number2)
        print(number_sum)
        return number_sum
    elif choice == "2" or choice.upper == "SUBSTRACTION":
        print('Please enter the numbers you would like to substract')
        number1 = input('Number 1: ')
        number2 = input('Number 2: ')
        number_diff = int(number1) - int(number2)
        print(number_diff)
        return number_diff
    elif choice == "3" or choice.upper == "MULTIPLICATION":
        print('Please enter the numbers you would like to multiply')
        number1 = input('Number 1: ')
        number2 = input('Number 2: ')
        number_mult = int(number1) * int(number2)
        print(number_mult)
        return number_mult
    elif choice == "4" or choice.upper == "DIVISION":
        print('Please enter the numbers you would like to divide')
        # Taken into an infinite loop in order to make user to enter valid values.
        while True:
            number1 = input('Numerator: ')
            number2 = input('Denominator: ')
            # Here one possible crash is prevented which is number divided by 0
            if number2 == "0" and number1 != "0":
                print('Division of any number with 0 is undefined.')
                print('Please re-enter your values.')
            # Here the other possible crash is prevented which is 0 divided by 0
            elif number1 == "0" and number2 == "0":
                print('Division of 0 over 0 is unidefined.')
                print('Please re-enter your values.')
            else:
                number_div = int(number1) / int(number2)
                print(number_div)
                return number_div
                
calculator()
