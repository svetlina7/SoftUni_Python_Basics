PRICE_ROSES = 5
PRICE_DAHLIAS = 3.80
PRICE_TULIPS = 2.80
PRICE_NARCISSUS = 3
PRICE_GLADIOLUS = 2.50

THRESHOLD_80 = 80
THRESHOLD_90 = 90
THRESHOLD_120 = 120

PERCENT_DISCOUNT_10 = 0.10
PERCENT_DISCOUNT_15 = 0.15
PERCENT_INCREASE_15 = 0.15
PERCENT_INCREASE_20 = 0.20

type_flowers = input()
count_flowers = int(input())
budjet = int(input())

price_flowers = 0

if type_flowers == 'Roses':
    price_flowers += (count_flowers * PRICE_ROSES)
    if count_flowers > THRESHOLD_80:
        price_flowers -= (price_flowers * PERCENT_DISCOUNT_10)

elif type_flowers == 'Dahlias':
    price_flowers += (count_flowers * PRICE_DAHLIAS)
    if count_flowers > THRESHOLD_90:
        price_flowers -= (price_flowers * PERCENT_DISCOUNT_15)

elif type_flowers == 'Tulips':
    price_flowers += (count_flowers * PRICE_TULIPS)
    if count_flowers > THRESHOLD_80:
        price_flowers -= (price_flowers * PERCENT_DISCOUNT_15)

elif type_flowers == 'Narcissus':
    price_flowers += (count_flowers * PRICE_NARCISSUS)
    if count_flowers < THRESHOLD_120:
        price_flowers += (price_flowers * PERCENT_INCREASE_15)

elif type_flowers == 'Gladiolus':
    price_flowers += (count_flowers * PRICE_GLADIOLUS)
    if count_flowers < THRESHOLD_80:
        price_flowers += (price_flowers * PERCENT_INCREASE_20)


if budjet >= price_flowers:
    print(f'Hey, you have a great garden with {count_flowers} {type_flowers} and {budjet - price_flowers:.2f} leva left.')
else:
    print(f"Not enough money, you need {price_flowers - budjet:.2f} leva more.")



