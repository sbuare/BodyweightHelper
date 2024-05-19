
# utils.py

import sys

def clear(row=1, col=1):
    # clears the console to a specified row and col
        # \033[r;cH moves cursor to row r col c
        # \033[0J clears from cursor to end
    
    str = f'\033[{row};{col}H\033[0J'
    print(u'%', str)

def exit(exit_str):
    # clears the console and exits the program
    
    clear()
    sys.exit(exit_str)