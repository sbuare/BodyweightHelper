from workout import Workout
from exercise import Exercise

user_workout_plans = []

def main_menu():
    print('Welcome')
    main_menu_str = ('Select options:\n'
                     '\t1. Create workout\n'
                     '\t2. View workout\n'
                     '\t3. Log workout\n')
    menu = int(input(main_menu_str))

    if menu == 1:
        print('Bringing you to creation menu...')
        # call creation funct here
    elif menu == 2:
        print('Displaying workouts...')
        # call viewing funct here
    elif menu == 3:
        print('Bringing you to logging menu...')
        # call logging funct here
    else:
        print('Invalid input. Please try again')
        main_menu()


def display_plans():
    global user_workout_plans
    
    print('Workout plans:\n')
    for plan in user_workout_plans:
        plan.preview()
      
my_squats = Exercise('Squats', 3)
my_pullups = Exercise('Pullups', 1)
my_exercises = [my_squats, my_pullups]

my_first_workout = Workout('First workout', '1-1-1', my_exercises, [5, 4, 4])
user_workout_plans.append(my_first_workout)

my_first_workout.display()




