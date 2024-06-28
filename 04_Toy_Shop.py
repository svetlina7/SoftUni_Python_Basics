PUZZLE = 2.60
DOLL = 3
BEAR = 4.10
MINION = 8.20
CAR = 2
NEEDED_TOYS_FOR_DISCOUNT = 50
PERCENT_DISCOUNT = 0.25
PERCENT_RENT = 0.10

price_traveling = float(input())
count_puzzle = int(input())
count_doll = int(input())
count_bear = int(input())
count_minion = int(input())
count_car = int(input())

count_toys = count_puzzle + count_doll + count_bear \
             + count_minion + count_car
sum_toys = (count_puzzle*PUZZLE) + (count_doll*DOLL) \
           + (count_bear*BEAR) \
           + (count_minion*MINION) + (count_car*CAR)

if count_toys>= NEEDED_TOYS_FOR_DISCOUNT:
    sum_toys-=(sum_toys*PERCENT_DISCOUNT)

sum_toys -= (sum_toys*PERCENT_RENT)

if sum_toys >= price_traveling:
    print(f'Yes! {sum_toys-price_traveling:.2f} lv left.')
else:
    print(f'Not enough money! {price_traveling-sum_toys:.2f} lv needed.')



