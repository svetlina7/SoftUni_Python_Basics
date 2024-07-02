GOAL_STEP_DAY = 10_000

# Goal reached! Good job!" {разликата между стъпките} steps over the goal!"
#
# Going home "{разликата между стъпките} more steps to reach goal

sum_steps = 0

while sum_steps < GOAL_STEP_DAY:
    steps = input()

    if steps == 'Going home':
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break

    sum_steps += int(steps)

result = ''

if sum_steps >= GOAL_STEP_DAY:
    result = f'Goal reached! Good job!\n{sum_steps-GOAL_STEP_DAY} steps over the goal!'
else:
    result = f'{GOAL_STEP_DAY-sum_steps} more steps to reach goal.'

print(result)

