import sys

n = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize

for _ in range(n):
    curr_number = int(input())
    if curr_number < min_number:
        min_number = curr_number

    if curr_number > max_number:
        max_number = curr_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')