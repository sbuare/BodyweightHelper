
# menus.py

from processing import create, view, log
from utils import clear, exit, handle_error

exit_str = 'Thank you for using the Bodyweight Helper :)'

def header():
    print('Welcome to the BodyweightHelper :)')
    print('To exit the program, enter -1.')


def creation_menu():
    # TODO: Store workout information in file
    clear()
    header()
    print('\nCreation menu')
    print('Select options: ')
    print('\t1. Create workout')
    print('\t2. Main menu')

    
def view_menu():  
    clear()
    header()
    print('\nView menu')
    print('Select options:')
    print('\t1. View workouts')
    print('\t2. Main menu')
                         

def log_menu():
    clear()
    header()
    print('\nLog menu')
    print('Select options:')
    print('\t1. Log workout')
    print('\t2. Main menu')


def main_menu():
    clear()
    header()
    print('\nMain menu')
    print('Select options:')
    print('\t1. Create workout')
    print('\t2. View workout')
    print('\t3. Log workout')
        
        
def main():
     
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
                        global_inp = int(input())
                        
                        if global_inp == 1: # 1. View workouts
                            clear()
                            view()                            
                        elif global_inp == 2: # 2. Main menu
                            break
                        else:
                            if global_inp == -1: # -1. Exit program
                                exit(exit_str)
                            else:
                                raise ValueError
                        
                    except Exception as e:
                        handle_error(e)


                        
            elif global_inp == 3:
                
                
                while True:
                    try:
                        
                        # Log menu section
                        log_menu()
                        global_inp = int(input())
                        
                        if global_inp == 1: # 1. Log workout
                            clear()
                            log()
                        elif global_inp == 2: # 2. Main menu
                            break
                        else:
                            if global_inp == -1: # -1. Exit program
                                exit(exit_str)
                            else:
                                raise ValueError
                                                
                    except Exception as e:
                        handle_error(e)
                        
                        
                        
            else:
                if global_inp == -1:
                    exit(exit_str)
                else:
                    raise ValueError
            
        except Exception as e:
            handle_error(e)
            
            
        