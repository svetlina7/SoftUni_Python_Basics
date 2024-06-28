n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    curr_num = int(input())
    left_sum += curr_num

for _ in range(n):
    curr_num = int(input())
    right_sum += curr_num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')