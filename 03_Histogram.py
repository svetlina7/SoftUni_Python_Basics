n = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

THRESHOLD_FOR_P1 = 200
THRESHOLD_FOR_P2 = 400
THRESHOLD_FOR_P3 = 600
THRESHOLD_FOR_P4 = 800

for num in range(n):
    number = int(input())

    if number < THRESHOLD_FOR_P1:
        count_p1 += 1
    elif number < THRESHOLD_FOR_P2:
        count_p2 += 1
    elif number < THRESHOLD_FOR_P3:
        count_p3 += 1
    elif number < THRESHOLD_FOR_P4:
        count_p4 += 1
    else:
        count_p5 += 1

total_count_p = count_p1+count_p2+count_p3+count_p4+count_p5

print(f'{count_p1 / total_count_p * 100:.2f}%')
print(f'{count_p2 / total_count_p * 100:.2f}%')
print(f'{count_p3 / total_count_p * 100:.2f}%')
print(f'{count_p4 / total_count_p * 100:.2f}%')
print(f'{count_p5 / total_count_p * 100:.2f}%')