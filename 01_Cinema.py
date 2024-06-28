PRICE_PREMIERE = 12
PRICE_NORMAL = 7.50
PRICE_DISCOUNT = 5

type_movie = input()
rows = int(input())
columns = int(input())


cinema_placements = rows * columns
price_cinema = 0

if type_movie == 'Premiere':
    price_cinema += cinema_placements * PRICE_PREMIERE
elif type_movie == 'Normal':
    price_cinema += cinema_placements * PRICE_NORMAL
else:
    price_cinema += cinema_placements * PRICE_DISCOUNT

print(f'{price_cinema:.2f} leva')


