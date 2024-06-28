# time = int(input())
# day = input()
#
# if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day== 'Thursday' or day == 'Friday' or day == 'Saturday'\
#         and time <= 10 and time <= 18:
#     print('open')
# else:
#     print('closed')

time = int(input())
weekday = input()

if 10 <= time <= 18 and (weekday == "Monday" or
                         weekday == "Tuesday" or
                         weekday == "Wednesday" or
                         weekday == "Thursday" or
                         weekday == "Friday" or weekday == 'Saturday'):
    print("open")
else:
    print("closed")