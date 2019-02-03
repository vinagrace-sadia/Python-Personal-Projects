import time


def add(num1, num2):
    return int(num1) + int(num2)


def subtract(num1, num2):
    return int(num1) - int(num2)


def multiply(num1, num2):
    return int(num1) * int(num2)


def divide(num1, num2):
    return int(num1) / int(num2)


def main():
    print('Select an operation:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')

    choice = input('Enter the number of your choice: ')

    while choice not in ['1', '2', '3', '4']:
        print('Invalid input. Please try again.')
        time.sleep(0.5)
        choice = input('Enter the number of your choice: ')

    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))
    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))
    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1, num2))


main()
