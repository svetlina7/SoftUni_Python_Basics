import math

figure = input() #'square', 'rectangle', 'circle', 'triangle'

if figure == 'square':
    side_a = float(input())
    area = side_a * side_a

elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif figure == 'circle':
    radius = float(input())
    area = math.pi * radius * radius

elif figure == 'triangle':
    side_a = float(input())
    h_a =float(input())
    area = side_a * h_a / 2

print(f'{area :.3f}')