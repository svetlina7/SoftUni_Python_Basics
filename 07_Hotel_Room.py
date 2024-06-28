PRICE_MAY_OCT_STUDIO = 50
PRICE_MAY_OCT_FLAT = 65
PRICE_JUNE_SEPT_STUDIO = 75.20
PRICE_JUNE_SEPT_FLAT = 68.70
PRICE_JULY_AUG_STUDIO = 76
PRICE_JULY_AUG_FLAT = 77

DISCOUNT_5 = 0.05
DISCOUNT_10 = 0.10
DISCOUNT_20 = 0.20
DISCOUNT_30 = 0.30

THRESHOLD_NIGHTS_7 = 7
THRESHOLD_NIHTS_14 =14

type_room = ''

month = input()
count_nights = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio += (count_nights * PRICE_MAY_OCT_STUDIO)
    price_apartment += (count_nights * PRICE_MAY_OCT_FLAT)
    if count_nights > THRESHOLD_NIHTS_14:
        price_studio -= (price_studio * DISCOUNT_30)
    elif count_nights > THRESHOLD_NIGHTS_7:
        price_studio -= (price_studio * DISCOUNT_5)

elif month == 'June' or month == 'September':
    price_studio += (count_nights * PRICE_JUNE_SEPT_STUDIO)
    price_apartment += (count_nights * PRICE_JUNE_SEPT_FLAT)
    if count_nights > THRESHOLD_NIHTS_14:
        price_studio -= (price_studio * DISCOUNT_20)

elif month == 'July' or month == 'August':
    price_studio += (count_nights * PRICE_JULY_AUG_STUDIO)
    price_apartment += (count_nights * PRICE_JULY_AUG_FLAT)

if count_nights > THRESHOLD_NIHTS_14:
    price_apartment -= (price_studio * DISCOUNT_10)

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_apartment:.2f} lv.')

