total_space = int(input()) * int(input()) * int(input())

cubic_meters = 0
result = ''

while total_space > cubic_meters:
    box= input()

    if box == 'Done':
        result = f'{total_space - cubic_meters} Cubic meters left.'
        break

    cubic_meters += int(box)

else:
    result = f'No more free space! You need {cubic_meters - total_space} Cubic meters more.'

print(result)