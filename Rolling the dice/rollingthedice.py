import random


def main():

    min_num = 1

    max_num = 6

    roll_again = 'yes'

    while roll_again == 'yes' or roll_again == 'y':
        print('Rolling the dice . . .')
        print('The values are:')

        print(random.randint(min_num, max_num))
        print(random.randint(min_num, max_num))

        roll_again = input('Roll dices again?')


main()
