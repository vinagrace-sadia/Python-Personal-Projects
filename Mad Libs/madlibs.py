import time


def main():
    print('Welcome to Mad Libs Generator.')
    time.sleep(1)
    print('Please select a story:')
    time.sleep(1)
    print('1. Summer Trip')
    time.sleep(0.5)
    print('2. Pretty Princess')
    time.sleep(0.5)
    print('3. A Trip to the Beach')
    time.sleep(0.5)
    print('4. Road Trip')
    time.sleep(0.5)
    print('5. The Longest Day of the Year \n')
    time.sleep(0.5)

    choice = input('Enter the number of choice: ')

    while choice not in ['1', '2', '3', '4', '5']:
        print('Invalid input. Please try again.')
        time.sleep(0.5)
        choice = input('Enter the number of your choice: ')

    if choice == '1':
        import summertrip
    elif choice == '2':
        import prettyprincess
    elif choice == '3':
        import triptobeach
    elif choice == '4':
        import roadtrip
    elif choice == '5':
        import longestday


main()
