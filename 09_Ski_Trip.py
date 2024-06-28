PRICE_ROOM_FOR_ONE_PERSON = 18
PRICE_ROOM_FOR_APARTMENT = 25
PRICE_ROOM_FOR_PRESIDENT_APARTMENT = 35

THRESHOLD_FOR_DISC_10 = 10
THRESHOLD_FOR_DISC_15 = 15

PERCENT_DISC_FOR_APARTMENT_30 = 0.30
PERCENT_DISC_FOR_APARTMENT_35 = 0.35
PERCENT_DISC_FOR_APARTMENT_50 = 0.50
PERCENT_DISC_FOR_PRESIDENT_APARTMENT_10 = 0.10
PERCENT_DISC_FOR_PRESIDENT_APARTMENT_15 = 0.15
PERCENT_DISC_FOR_PRESIDENT_APARTMENT_20 = 0.20
ADDITIONAL_INCREASE_PERCENT_25 = 0.25
ADDITIONAL_DISC_PERCENT_10 = 0.10

count_days = int(input()) - 1
type_room = input()
assesment = input()

price = 0

if type_room == 'room for one person':
    price+= (count_days * PRICE_ROOM_FOR_ONE_PERSON)

elif type_room == 'apartment':
    price += (count_days * PRICE_ROOM_FOR_APARTMENT)
    if count_days <THRESHOLD_FOR_DISC_10:
        price -= (price * PERCENT_DISC_FOR_APARTMENT_30)
    elif THRESHOLD_FOR_DISC_10 <= count_days <= THRESHOLD_FOR_DISC_15:
        price -= (price * PERCENT_DISC_FOR_APARTMENT_35)
    elif count_days > THRESHOLD_FOR_DISC_15:
        price -= (price * PERCENT_DISC_FOR_APARTMENT_50)
else:
    price += (count_days * PRICE_ROOM_FOR_PRESIDENT_APARTMENT)

    if count_days < THRESHOLD_FOR_DISC_10:
        price -= (price * PERCENT_DISC_FOR_PRESIDENT_APARTMENT_10)
    elif THRESHOLD_FOR_DISC_10 <= count_days <= THRESHOLD_FOR_DISC_15:
        price -= (price * PERCENT_DISC_FOR_PRESIDENT_APARTMENT_15)
    elif count_days > THRESHOLD_FOR_DISC_15:
        price -= (price * PERCENT_DISC_FOR_PRESIDENT_APARTMENT_20)

if assesment == 'positive':
    price += (price * ADDITIONAL_INCREASE_PERCENT_25)
else:
    price -= (price * ADDITIONAL_DISC_PERCENT_10)

print (f'{price:.2f}')


