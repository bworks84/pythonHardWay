while True:  # if the while condition is true if block is executed
    a = input('Do you want to continue or not (Y / N)? ')
    # If the user pass 'Y', the following statement is executed.
    if a.upper() != 'Y':
        break

    a = int(input(' First number is: '))  # first number
    b = int(input(' Second number is: '))  # second number
    print(a, ' % ', b, ' = ', a % b)  # perform a % b
    print(b, ' % ', a, ' = ', b % a)  # perform b % a
