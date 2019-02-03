import time


def main():
    person = input('\nWhat\'s the name of your best friend? ')
    place = input('Your favorite place: ')
    adjective1 = input('What\'s the weather like today? ')
    plural_noun1 = input('What can you find at your favorite place? ')
    adjective2 = input('Enter a random adjective: ')
    plural_noun2 = input('Enter a random plural noun: ')
    place2 = input('Your next favorite place: ')
    action_verb1 = input('What do you usually do there? ')
    plural_noun3 = input('What do you usually go to see there? ')
    plural_noun4 = input('Enter a plural noun that you can eat: ')
    noun1 = input('Enter a random object: ')
    action_verb2 = input('Your favorite thing to do under the sun: ')
    action_verb3 = input('Another favorite thing to do: ')
    noun2 = input('Enter a noun in relation your answer above: ')
    adjective = input('Describe the trip: ')

    time.sleep(0.5)
    print('\nCreating your Mad Lib.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(1)
    print('Done! \n\n')
    time.sleep(1)

    print(f'Last summer, my mom and dad took me and {person} on a trip to {place}.'
          f'The weather there is very {adjective1}! Northern {place} has many {plural_noun1}, and they make '
          f'{adjective2} {plural_noun2} there.\n'
          f'Many people also goes to {place2} to {action_verb1} or see the {plural_noun3}. The people that live there '
          f'love to eat {plural_noun4} and are very proud of there big {noun1}. They also like to {action_verb2} '
          f'in the sun and {action_verb3} in the {noun2}! It was a really {adjective} trip!')


main()
