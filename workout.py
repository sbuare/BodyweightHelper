
# workout.py

from exercise import Exercise


class Workout:
    
    user_workout_plans = []
    
    def __init__(self, name, date, exercises):
        self.name = name
        self.date = date
        self.exercises = exercises # list of Exercise objects
        Workout.user_workout_plans.append(self)

    def preview(self):
        disp = (f' - {self.name}, created {self.date}.\n'
                f'\tExercises: {self.exercises}, 3 sets of {self.routine}.')
        print(disp)

    def display(self):
        routine_strings = ''
        for exer in self.exercises:
          exer_line = (f'\n\t{exer.diff_name}, difficulty {exer.diff}: '
                       f'\n\t\t{exer.routine[0]} reps, rest 1-2 min'
                       f'\n\t\t{exer.routine[1]} reps, rest 1-2 min'
                       f'\n\t\t{exer.routine[2]} reps, rest 1-2 min')
          routine_strings += exer_line
    
        disp = (f' Workout: {self.name}' 
                f'\n Created: {self.date}'
                f'\n Routine:' 
                f'\n\t10 minute warm up (dynamic stretching)'
                f'{routine_strings}'
                f'\n\t10 minute cool down (static stretching)')
        print(disp)
    
    @classmethod
    def display_plans(cls):
        print('Workout plans:\n')
        for plan in cls.user_workout_plans:
            plan.preview()
    
    def log(self):
        
        # Workout.log() updates exercise info based on the following parameters:
            # If the exercise is at max difficulty with a 3x8 routine,
                # Do not change the information
            # If the exercise has a 3x8 routine,
                # Increase the difficulty by one and reset the routine to 3x4
            # Otherwise,
                # Increment the first element of the array that is not greater
                # than any other element in the array
                # Ex: 444 becomes 544, 544 becomes 554, 554 becomes 555, etc.
        
        for exer in self.exercises:
            if exer.routine == [8, 8, 8] and exer.diff == exer.max_diff:
                continue
            elif exer.routine == [8, 8, 8]:
                exer.diff += 1
                exer.routine = [4, 4, 4]
            else:
                incr = True
                for i in range(len(exer.routine)):
                    for j in range(len(exer.routine)):
                        if exer.routine[i] > exer.routine[j]:
                            incr = False
                            break
                    if incr:
                        exer.routine[i] += 1
                        break
                    else:
                        incr = True
        
        print('Workout logged. Nice job, be sure to rest tomorrow.')
        print('Your next workout will be: ')
        print()
        self.display()
  
  
if __name__ == '__main__':
    
    my_squats = Exercise('Squats', 3, [4, 4, 4])
    my_pullups = Exercise('Pullups', 2, [8, 8, 8])
    my_wo = Workout('my woahh', '1-1-1', [my_squats, my_pullups])

    print(f'Max difficulty of squats: {my_squats.max_diff}')
    print(f'Max difficulty of pullups: {my_pullups.max_diff}')
    
    my_wo.display()
    print()
    print('Logging:')
    print()
    my_wo.log()
            
            
