import time
import random


def main():
    player = input('What\'s your name? ')
    print('Hello,', player + '.', 'Time to play Hangman!')

    time.sleep(1)

    print('Start guessing . . .')

    time.sleep(0.5)

    # Lists of possible words to guess
    words = [
        'bacon',
        'grass',
        'flowers',
        'chair',
        'fruit',
        'morning',
        'games',
        'queen',
        'secret',
        'funny'
    ]

    word = words[random.randint(0, len(words) - 1)]
    turns = 10
    guesses = ''

    while turns > 0:
        # The number of letters or characters to find
        char_to_find = 0

        for char in word:
            if char in guesses:
                print(char)
            else:
                char_to_find += 1
                print('_')

        # When all the characters of the word are found
        if char_to_find == 0:
            print('Congratulations! You won!')
            print('The word we\'re looking for is: ', word + '.')
            break

        guess = input('Guess the letter: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Wrong!')

        if turns == 0:
            print('Game Over. You Loose.')
        else:
            print('You have', turns, 'turn(s) left. More guesses.')


main()
