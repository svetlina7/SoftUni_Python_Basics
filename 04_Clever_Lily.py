BROTHER_MONEY = 1
INCREASE_MONEY_FOR_BD = 10

years = int(input())
price_washing_machine = float(input())
price_toy = int(input())

birthday_money = 10
count_toys = 0
total_money = 0

for year in range (1, years +1):
    if year % 2 == 0:
        total_money += (birthday_money - BROTHER_MONEY)
        birthday_money += INCREASE_MONEY_FOR_BD
    else:
        count_toys += 1

total_money += (count_toys * price_toy)

result = ''

if total_money >= price_washing_machine:
    result = f'Yes! {total_money - price_washing_machine:.2f}'
else:
    result = f'No! {price_washing_machine - total_money:.2f}'

print(result)