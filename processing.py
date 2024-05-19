
# processing.py

from datetime import date

from exercise import Exercise
from utils import clear
from workout import Workout

def create():
  
    global user_workout_plans

    name = input('What would you like to name this workout?\n')
    todays_date = date.today()

    exer_str = ('Please select the exercises you want to include (-1 to finish):\n'
        '\t1. Squats\n'
        '\t2. Pullups\n')
    exer_inp = int(input(exer_str))
    exer_set = set()

    while exer_inp != -1:
        if exer_inp == 1:
            exer_set.add('Squats')
        elif exer_inp == 2:
            exer_set.add('Pullups')
        else:
            print('Invalid input. Please try again.')

    clear(3, 1)
    exer_inp = int(input(exer_str))

    diff_inp = 0
    exer_obj_list = []

    for exer in exer_set:
    clear(3, 1)
    diff_str = ('Please select the difficulty of the exercise '
                '(-1 if unsure. Default is 1.):\n'
                + Exercise.info(exer))

    diff_inp = int(input(diff_str))

    if diff_inp == -1:
        exer_obj_list.append(Exercise(exer))
    else:
        exer_obj_list.append(Exercise(exer, diff_inp))

    new_wo = Workout(name, todays_date, exer_obj_list)
    
    return new_wo