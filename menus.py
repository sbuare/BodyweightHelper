
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
    clear()
    header()
    print('Creation menu')
    print('Select options: ')
    print('\t1. Create workout')
    print('\t2. Main menu')

    
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
    clear()
    header()
    print('\nMain menu')
    print('Select options:')
    print('\t1. Create workout')
    print('\t2. View workout')
    print('\t3. Log workout')
        
        
def main():

    global global_inp
    
    
    while True:
        try:
            
            # Main menu section
            main_menu()
            global_inp = int(input())

            if global_inp == 1:
                
                
                while True:
                    try:
                        
                        # Creation menu section
                        creation_menu() 
                        global_inp = int(input())

                        if global_inp == 1: # 1. Create workout
                            clear()
                            create()
                        elif global_inp == 2: # 2. Main menu
                            break
                        else:
                            if global_inp == -1: # -1. Exit program
                                exit(exit_str)
                            else:
                                raise ValueError

                    except Exception as e:
                        handle_error(e)
            

            
            elif global_inp == 2:
                
                
                while True:
                    try:
                    
                        # View menu section
                        view_menu()
                        break
                        
                    except Exception as e:
                        handle_error(e)


                        
            elif global_inp == 3:
                
                
                while True:
                    try:
                        
                        # Log menu section
                        log_menu()
                        break
                        
                    except Exception as e:
                        handle_error(e)
                        
                        
                        
            else:
                if global_inp == -1:
                    exit(exit_str)
                else:
                    raise ValueError
            
        except Exception as e:
            handle_error(e)
            
            
        