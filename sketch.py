
'''
Bodyweight Helper Sketch

TODO 5-14-24:
 - Integrate different exercise variations (contained in squats list) into Workout class
 - Write the user input stuff
'''

# global vars
# a list of squat variations (stored in nested dictionaries)

squats = [
	1 : {
		'name' : 'Assisted squat'
		'desc' : """Rest your hands on the back of a chair in front you.\n
				  Lower yourself till your thighs are parallel with the floor,\n 
				  and come back up, using the chair as a support."""
	}
	2 : {
		'name' : 'Deep assisted squat'
		'desc' : """Rest your hands on the back of a chair in front you.\n
				  Squat through the full range of motion and come back up,\n
				  using the chair as a support."""
	}
	3 : {
		'name' : 'Squats'
		'desc' : """Without any help, lower yourself till your thighs are\n
					parallel with the floor, and come back up."""
	}
]

# a list of routines the user created
user_workout_plans = []

def display_plans():
    # iterates user_workout_plans and calls Workout.preview() for each plan
    global user_workout_plans
    
    print('Workout plans:\n')
    for plan in user_workout_plans:
        plan.preview()

# main menu at startup
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


# Exercise class
class Exercise:
    def __init__(self, name, difficulty=1):
        self.name = name
        self.difficulty = difficulty
    
    def display(self):
        print(f'{self.name}, difficulty level {self.difficulty}')

# Workout class
class Workout:
    def __init__(self, name, date, exercises, routine=None):
        global user_workout_plans
        
        self.name = name
        self.date = date
        self.exercises = exercises # list of Exercise objects
        self.routine = [4, 4, 4] if routine is None else routine
        
        user_workout_plans.append(self)

    def preview(self): # prints a preview of the Workout object
        disp = (f' - {self.name}, created {self.date}.\n'
                f'\tExercises: {self.exercises}, 3 sets of {self.routine}.')
        print(disp)

    def display(self): # prints entire Workout routine with time blocks
        routine_strings = ''
        for exer in self.exercises: # loop through each exercise in list
          exer_line = f'\n\t{exer.getName()}, difficulty{exer.getDiff()}: {routine[0]} reps, '
          routine_strings += exer_line
    
        disp = (f' Workout: {self.name}' 
                f'\n Created: {self.date}'
                f'\n Routine:' 
                f'\n\t10 minute warm up (dynamic stretching)'
                f'{routine_strings}')
        print(disp)
      

my_first_workout = Workout('First workout', '1-1-1', ['Squats', 'Pullups'], [5, 4, 4])

my_first_workout.display()




