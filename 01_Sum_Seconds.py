SECONDS_IN_MINUTES = 60

time_first = int(input()) #30
time_seconds = int(input()) #20
time_third = int(input()) #30

sum_seconds = time_first+time_seconds+time_third  # 30+20-30= 80
minutes = sum_seconds // SECONDS_IN_MINUTES
seconds = sum_seconds % SECONDS_IN_MINUTES

print(f'{minutes}:{seconds:02d}')

# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')

