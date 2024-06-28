MINUTES_IN_ONE_HOUR = 60

exam_hour = int(input())
exam_minute = int(input())
arrived_hour = int(input())
arrived_minute = int(input())

exam_minutes = exam_hour * MINUTES_IN_ONE_HOUR + exam_minute
arrived_minute = arrived_hour * MINUTES_IN_ONE_HOUR + arrived_minute

time_diff = exam_minutes - arrived_minute

if time_diff > 30:
    print('Early')
elif time_diff < 0:
    print('Late')
else:
    print('On time')

hours = abs(time_diff) // MINUTES_IN_ONE_HOUR
minutes = abs(time_diff) % MINUTES_IN_ONE_HOUR

result = ''

if hours > 0:
    result += f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'

if time_diff > 0:
    result += ' before the start'
elif time_diff < 0:
    result += ' after the start'

print(result)