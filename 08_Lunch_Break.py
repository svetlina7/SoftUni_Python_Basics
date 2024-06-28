import math

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

time_lunch = break_duration / 8
time_chill = break_duration / 4

needed_time_for_all = time_lunch + time_chill + episode_duration
time_left = break_duration - needed_time_for_all

if time_left >= 0:
    print(f'You have enough time to watch {serial_name} and left with {math.ceil(time_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(abs(time_left))} more minutes.")
