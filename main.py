
# main.py

from menus import global_inp, main_menu

if __name__ == '__main__':
    print('Welcome to the BodyweightHelper :)')
    print('To exit the program, enter -1.')

    while global_inp != -1:
        main_menu()
