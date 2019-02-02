import random


def main():
    min_num = 1
    max_num = 99

    rand_num = random.randint(min_num, max_num)
    guess = int(input('Enter an integer from ' + str(min_num) + ' to ' + str(max_num) + ': '))

    while rand_num != guess:
        if guess < rand_num:
            print('Your guess is low.')
            guess = int(input('Enter an integer from ' + str(min_num) + ' to ' + str(max_num) + ': '))
        elif guess > rand_num:
            print('Your guess is higher.')
            guess = int(input('Enter an integer from ' + str(min_num) + ' to ' + str(max_num) + ': '))

    print('You guessed it! The answer is: ' + str(rand_num))


main()


