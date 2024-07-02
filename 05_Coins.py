COINS_200 = 200
COUNS_100 = 100
COINS_50 = 50
COINS_20 = 20
COINS_10 = 10
COINS_5 = 5
COINS_2 = 2
COINS_1 = 1

change = int(float(input()) * 100)

coins_count = 0

while change > 0:

    if change >=COINS_200:
        change -= COINS_200

    elif change >= COUNS_100:
        change -= COUNS_100

    elif change >= COINS_50:
        change -= COINS_50

    elif change >= COINS_20:
        change -= COINS_20

    elif change >= COINS_10:
        change -= COINS_10

    elif change >= COINS_5:
        change -= COINS_5

    elif change >= COINS_2:
        change -= COINS_2

    elif change >= COINS_1:
        change -= COINS_1

    coins_count += 1

print(coins_count)