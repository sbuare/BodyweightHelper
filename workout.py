
# workout.py

class Workout:
    def __init__(self, name, date, exercises, routine=None):
        self.name = name
        self.date = date
        self.exercises = exercises # list of Exercise objects
        self.routine = [4, 4, 4] if routine is None else routine

    def preview(self): # prints a preview of the Workout object
        disp = (f' - {self.name}, created {self.date}.\n'
                f'\tExercises: {self.exercises}, 3 sets of {self.routine}.')
        print(disp)

    def display(self): # prints entire Workout routine with time blocks
        routine_strings = ''
        for exer in self.exercises: # loop through each exercise in list
          exer_line = (f'\n\t{exer.diff_name}, difficulty {exer.diff}: '
                       f'\n\t\t{self.routine[0]} reps, rest 1-2 min'
                       f'\n\t\t{self.routine[1]} reps, rest 1-2 min'
                       f'\n\t\t{self.routine[2]} reps, rest 1-2 min')
          routine_strings += exer_line
    
        disp = (f' Workout: {self.name}' 
                f'\n Created: {self.date}'
                f'\n Routine:' 
                f'\n\t10 minute warm up (dynamic stretching)'
                f'{routine_strings}'
                f'\n\t10 minute cool down (static stretching)'
                f'\n Done, congrats!')
        print(disp)