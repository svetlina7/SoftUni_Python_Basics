THRESHOLD_BAD_GRADE = 4

sum_grades = 0
total_count_solved_tasks = 0
count_bad_grades = 0
last_task = ''
result = ''

allowed_bad_grades = int(input())

while allowed_bad_grades > count_bad_grades:
    task_name = input()

    if task_name == 'Enough':
        result = f'Average score: {sum_grades /total_count_solved_tasks:.2f}\n'\
                f'Number of problems: {total_count_solved_tasks}\n' \
                 f'Last problem: {last_task}'
        break

    grade = int(input())

    if grade <= THRESHOLD_BAD_GRADE:
        count_bad_grades +=1

    sum_grades += grade
    total_count_solved_tasks += 1
    last_task = task_name

else:
    result = f'You need a break, {count_bad_grades} poor grades.'

print(result)