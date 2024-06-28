MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
ADDITIONAL_MINUTES = 15

hours = int(input())
minutes = int(input())

minutes += ADDITIONAL_MINUTES

if minutes >= MINUTES_IN_HOUR:
    minutes -= MINUTES_IN_HOUR
    hours += 1

if hours >= HOURS_IN_DAY:
    hours -= HOURS_IN_DAY

print(f'{hours}:{minutes:02d}')