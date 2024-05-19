
# menus.py
from processing import create
from utils import clear, exit

global_inp = 0
exit_str = 'Thank you for using the Bodyweight Helper :)'

def create_menu():
    # TODO: Store workout information in file

    global global_inp

    clear(3, 1)
    print('Creation menu')
    print('Select options: ')
    print('\t1. Create workout')
    print('\t2. Main menu')

    global_inp = int(input())

    if global_inp == 1:
        clear(4, 1)
        create()
        create_menu()
    elif global_inp == 2:
        return
    else:
        if global_inp == -1:
            exit(exit_str)
        else:
            print('Invalid input. Please try again.')
            create_menu()

def view():
    # TODO: Display workouts
    # Actual print()s will be in Workout class
    # view() will create the user interaction loops for selecting what to display
    pass

def log():
    # TODO: Prompt selection of workout
    # Display workout, ask for confirmation
    # Update workout info
    pass

def main_menu():
    global global_inp

    clear(3, 1)
    print('Main menu')
    main_menu_str = ('Select options:\n'
                     '\t1. Create workout\n'
                     '\t2. View workout\n'
                     '\t3. Log workout\n')

    global_inp = int(input(main_menu_str))

    if global_inp == 1:
        create_menu()
    elif global_inp == 2:
        view()
    elif global_inp == 3:
        log()
    else:
        if global_inp == -1:
            exit(exit_str)
        else:
            print('Invalid input. Please try again.')
            main_menu()