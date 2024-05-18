from workout import Workout
from exercise import Exercise
import sys

user_workout_plans = []
global_inp = 0

def display_plans():
    global user_workout_plans
    
    print('Workout plans:\n')
    for plan in user_workout_plans:
        plan.preview()

def clear():
    # \033[3;1H moves cursor to row 3 col 1
    # \033[0J clears from cursor to end
    print(u'\033[3;1H\033[0J')

def exit():
    clear()
    sys.exit('Thank you for using the Bodyweight Helper :)')

def create():
    # TODO: User interaction returning new Workout object
    # Store workout information in file

    global global_inp
    
    clear()
    print('Creation menu')
    print('Select options: ')
    print('\t1. Create workout')
    print('\t2. Main menu')

    global_inp = int(input())

    if global_inp == 1:
        # TODO: creation process
        print('Workout created.')
        create()
    elif global_inp == 2:
        return
    else:
        if global_inp == -1:
            exit()
        else:
            print('Invalid input. Please try again.')
            create()

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
    
    clear()
    print('Main menu')
    main_menu_str = ('Select options:\n'
                     '\t1. Create workout\n'
                     '\t2. View workout\n'
                     '\t3. Log workout\n')
    
    global_inp = int(input(main_menu_str))

    if global_inp == 1:
        create()
    elif global_inp == 2:
        view()
    elif global_inp == 3:
        log()
    else:
        if global_inp == -1:
            exit()
        else:
            print('Invalid input. Please try again.')
            main_menu()


if __name__ == '__main__':
    print('Welcome to the BodyweightHelper :)')
    print('To exit the program, enter -1.')
    
    while global_inp != -1:
        main_menu()




