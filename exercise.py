
# exercise.py

from progressions import progressions

class Exercise:
    def __init__(self, name, diff=1):
        self.name = name
        self.diff = diff
        self.diff_name = progressions[self.name][self.diff].get('name')
        self.desc = progressions[self.name][self.diff].get('desc')