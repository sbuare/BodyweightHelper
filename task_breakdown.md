<h1>Bodyweight Helper Task Breakdown</h1>


(A writing exercise I gave myself to help mentally break down the project)


<h2>What is the big picture task?</h2>

A program that interacts with the user. It starts up, welcomes, then asks the user to choose between three options: create workout, view workout, log workout

If the user chooses view workout, it will display a list of all workout previews. The user can select one to see its full display. The user can choose to leave this viewing mode, first back to the previews, then back to the main menu.

If the user chooses create workout, the program will ask a series of questions and store and parse the responses:
- Name of workout, todays date (better to let it read the computers date)
- What exercises the user wishes to complete
    - What level of each exercise they are most comfortable with
    - If unsure, explain the method—see which exercise they can comfortably manage 4 of, then move down a level and start with 4
    - Default: easiest, 4 reps
- The repetition pattern - always set as 444

If the user logs a workout, the workout must be updated. The user will indicate they are logging, then select the workout they logged. The workout will update according to the following parameters:
- If the repetition pattern is not 888, update the repetition pattern
- If it is 888, set the pattern to 444 and increase the difficulty to the next level

An optional feature if there’s time - workout history and progress tracking


<h2>How can we break this into smaller tasks?</h2>

1. Create the user interface “shell” — set up the main menu
    1. Print welcome
    2. Print menu options and ask for input
2. At user’s selection of “View workouts”: 
    1. display the workouts
    2. At user’s selection of a specific workout, display the workout
    3. At user’s selection of “Back”, return to the list
    4. At user’s selection of “Back” or “Menu”, return to the main menu
3. At user’s selection of “Create workout”:
    1. Prompt name
    2. Select exercises (while until stop)
        1. Display difficulty levels and descriptions
        2. Select difficulty of each exercise (try them out yourself. Whichever one you are comfortable doing 4 of, choose one stage before it.)
        3. Otherwise, select easiest
    3. Create Workout object with name, current date, chosen exercises, and 444 pattern
    4. Print “workout created!”
    5. Display the workout 
    6. At user’s selection of “menu”, return to menu
4. At user’s selection of “Log workout”:
    1. Display workout
    2. Update the workout according to the following rules:
        1. If the repetition pattern is not 888, update the repetition pattern
        2. If it is 888, set the pattern to 444 and increase the difficulty to the next level
    3. Print “nice job. Rest tomorrow, then the day after come back and do this:
    4. Display updated workout
    5. At user’s selection of “menu”, return to menu