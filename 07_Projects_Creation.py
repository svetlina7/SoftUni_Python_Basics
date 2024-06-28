NEEDED_TIME_FOR_ONE_PROJECT = 3

name = input()
count_projects = input()

hours = int(count_projects) * NEEDED_TIME_FOR_ONE_PROJECT

print(f'The architect {name} will need {hours} hours to complete {count_projects} projects.')

