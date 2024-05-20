
# processing.py


from datetime import date

from exercise import Exercise
from utils import clear, handle_error
from workout import Workout


# creation_menu helper functions

def pick_exercises():
    # returns list of exercise names (str)
    
    clear()
    exer_str = ('Please select the exercises you want to include (-1 to finish):\n'
        '\t1. Squats\n'
        '\t2. Pullups\n')
    
    exer_set = set()
            
    while True: 
        try:
            
            clear()
            exer_inp = int(input(exer_str))
    
            if exer_inp == -1:
                break
            elif exer_inp == 1:
                print('Added squats.')
                exer_set.add('Squats')
            elif exer_inp == 2:
                print('Added pullups.')
                exer_set.add('Pullups')
            else:
                raise ValueError
        
        except Exception as e:
            handle_error(e)
        
  
    return sorted(exer_set)


def pick_diffs(exer_list):
    # returns list of Exercise objects with difficulties configured
    
    exer_objs = []
    
    i = 0
    while i < len(exer_list):
        try:
            
            clear()
            exer = exer_list[i]
            diff_str = ('Please select the difficulty of the exercise '
                        '(-1 if unsure. Default is 1.):\n'
                        + Exercise.info(exer))
            max_diff = Exercise.get_max_diff(exer)
            diff_inp = int(input(diff_str))
            
            if diff_inp > max_diff or diff_inp < 0:
                raise ValueError
            elif diff_inp == -1:
                exer_objs.append(Exercise(exer))
            else:
                exer_objs.append(Exercise(exer, diff_inp))
            
            i += 1
            
        except Exception as e:
            handle_error(e)
            
    return exer_objs
    

def create():
  
    name = input('What would you like to name this workout?\n')
    todays_date = date.today()

    clear()
    
    exer_list = pick_exercises()
    exer_obj_list = pick_diffs(exer_list)
        
    new_wo = Workout(name, todays_date, exer_obj_list)
    
    print('Workout created.')
    return new_wo
 
 
# view_menu helper functions

def view():
    view_str = 'Select a workout to see its details. -1 to go back.\n'
        
    while True:
        try:
            
            Workout.display_plans()
            view_inp = int(input(view_str))
            
            if view_inp == -1:
                break
            else:
                selected_wkout = Workout.user_workout_plans[view_inp-1]
                clear()
                selected_wkout.display()
            
        except Exception as e:
            handle_error(e)


# log_menu helper functions

def log():
    log_str = 'Select a workout to log. -1 to go back. \n'
    
    while True:
        try:
            
            Workout.display_plans()
            log_inp = int(input(log_str))
            
            if log_inp == -1:
                break
            else:
                selected_wkout = Workout.user_workout_plans[log_inp-1]
                selected_wkout.log()
    
        except Exception as e:
            handle_error(e)

