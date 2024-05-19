
# menus.py

# FIXME: Replace all recursive calls with while True w/ breaks!

from processing import create
from utils import clear, exit, handle_error

global_inp = 0
exit_str = 'Thank you for using the Bodyweight Helper :)'

def header():
    print('Welcome to the BodyweightHelper :)')
    print('To exit the program, enter -1.')

def creation_menu():
    # TODO: Store workout information in file

    global global_inp

    clear()
    print('Creation menu')
    print('Select options: ')
    print('\t1. Create workout')
    print('\t2. Main menu')


    try:
        global_inp = int(input())

        if global_inp == 1: # 1. Create workout
            clear()
            create()
            creation_menu()
        elif global_inp == 2: # 2. Main menu
            main_menu()
        else:
            if global_inp == -1: # -1. Exit program
                exit(exit_str)
            else:
                raise ValueError
    
    except Exception as e:
        handle_error(e)
        creation_menu()
 
    
def view_menu():
    # TODO: Display workouts
    # Actual print()s will be in Workout class
    # view() will create the user interaction loops for selecting what to display
    pass

def log_menu():
    # TODO: Prompt selection of workout
    # Display workout, ask for confirmation
    # Update workout info
    pass

def main_menu():
    global global_inp

    clear()
    header()
    print('\nMain menu')
    main_menu_str = ('Select options:\n'
                     '\t1. Create workout\n'
                     '\t2. View workout\n'
                     '\t3. Log workout\n')
    
    try:
        global_inp = int(input(main_menu_str))
    
        if global_inp == 1:
            creation_menu()
        elif global_inp == 2:
            view_menu()
        elif global_inp == 3:
            log_menu()
        else:
            if global_inp == -1:
                exit(exit_str)
            else:
                raise ValueError
        
    except Exception as e:
        handle_error(e)
        main_menu()