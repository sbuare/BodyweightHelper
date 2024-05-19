
# exercise.py

from progressions import progressions


class Exercise:
    def __init__(self, name, diff=1, routine=None):
        self.name = name
        self.diff = diff
        
        self.routine = [4, 4, 4] if routine is None else routine
        
        self.diff_name = progressions[self.name][self.diff].get('name')
        self.desc = progressions[self.name][self.diff].get('desc')
        self.max_diff = len(progressions[self.name])
        
    @staticmethod
    def info(exer_name):
        # returns exer_name's difficulties and descriptions from progressions
        # exer_name must match the formatting in progressions

        info_str = f'{exer_name}:'
        diff_info = progressions[exer_name]

        for lvl in diff_info:
            info_str += f'\n{lvl}. '
            
            for key, val in diff_info[lvl].items():
                info_str += f'\n{key}: {val}'
            
            info_str += '\n'
        
        return info_str
    
    @staticmethod
    def get_max_diff(exer_name):
        return len(progressions[exer_name])
            
    