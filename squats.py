
""" Welcome to the bodyweight fitness helper. This program assists in learning 
various bodyweight exercises that target all the muscle groups in your body, 
starting from the very basics! So far, only squats have been implemented.
For now, this is a program that can help people learn to do good squats. 

The information comes from an exercise program designed by Nick Janvier and is fully 
accessible from startbodyweight.com. The goal of this Python script is to design a 
user interface that can cleanly display the information in a format that is digestible,
which can help the user more easily begin the exercises."""

""" Interface of the program """
""" Opens to above welcome script.
    Options:
      - Create a workout plan
      - Display a workout plan
"""

'''
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

# Creating a workout plan
class Workout:
    def __init__(self, name, date, exercises, routine=None):
        global user_workout_plans
        
        self.name = name
        self.date = date
        self.exercises = exercises
        self.routine = [4, 4, 4] if routine is None else routine
        
        user_workout_plans.append(self)

    def preview(self): # prints a preview of the Workout object
        disp = (f' - {self.name}, created {self.date}.\n'
                f'\tExercises: {self.exercises}, 3 sets of {self.routine}.')
        print(disp)

    def display(self): # prints entire Workout routine with time blocks
        routine_strings = ''
        for exer in self.exercises:
          exer_line = f'\n\t{exer}: good luck lol'
          routine_strings += exer_line
    
        disp = (f' Workout: {self.name}' 
                f'\n Created: {self.date}'
                f'\n Routine:' 
                f'\n\t10 minute warm up (dynamic stretching)'
                f'{routine_strings}')
        print(disp)

my_first_workout = Workout('First workout', '1-1-1', ['Squats', 'Pullups'], [5, 4, 4])

my_first_workout.display()

