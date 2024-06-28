RENT_SPRING = 3000
RENT_SUMMER = 4200
RENT_AUTUMN = 4200
RENT_WINTER = 2600

THRESHOLD_FISHERMANS_6 = 6
THRESHOLD_FISHERMANS_7 = 7
THRESHOLD_FISHERMANS_11 = 11
THRESHOLD_FISHERMANS_12 = 12

PERCENT_DISCOUNT_5 = 0.05
PERCENT_DISCOUNT_10 = 0.10
PERCENT_DISCOUNT_15 = 0.15
PERCENT_DISCOUNT_25 = 0.25
ADDITIONAL_PERCENT_DISCOUNT_5 = 0.05

price_rent = 0

budjet = int(input())
season = input()
count_fishermans = int(input())

if season == 'Spring':
    price_rent = RENT_SPRING
    if count_fishermans <= THRESHOLD_FISHERMANS_6:
        price_rent -= (price_rent* PERCENT_DISCOUNT_10)
    elif THRESHOLD_FISHERMANS_7 < count_fishermans <= THRESHOLD_FISHERMANS_11:
        price_rent -= (price_rent * PERCENT_DISCOUNT_15)
    elif count_fishermans > THRESHOLD_FISHERMANS_12:
        price_rent -= (price_rent * PERCENT_DISCOUNT_25)

elif season == 'Summer':
    price_rent = RENT_SUMMER
    if count_fishermans <= THRESHOLD_FISHERMANS_6:
        price_rent -= (price_rent* PERCENT_DISCOUNT_10)
    elif THRESHOLD_FISHERMANS_7 < count_fishermans <= THRESHOLD_FISHERMANS_11:
        price_rent -= (price_rent * PERCENT_DISCOUNT_15)
    elif count_fishermans > THRESHOLD_FISHERMANS_12:
        price_rent -= (price_rent * PERCENT_DISCOUNT_25)


elif season == 'Autumn':
    price_rent = RENT_AUTUMN
    if count_fishermans <= THRESHOLD_FISHERMANS_6:
        price_rent -= (price_rent* PERCENT_DISCOUNT_10)
    elif THRESHOLD_FISHERMANS_7 < count_fishermans <= THRESHOLD_FISHERMANS_11:
        price_rent -= (price_rent * PERCENT_DISCOUNT_15)
    elif count_fishermans > THRESHOLD_FISHERMANS_12:
        price_rent -= (price_rent * PERCENT_DISCOUNT_25)

elif season == 'Winter':
    price_rent = RENT_WINTER
    if count_fishermans <= THRESHOLD_FISHERMANS_6:
        price_rent -= (price_rent * PERCENT_DISCOUNT_10)
    elif THRESHOLD_FISHERMANS_7 < count_fishermans <= THRESHOLD_FISHERMANS_11:
        price_rent -= (price_rent * PERCENT_DISCOUNT_15)
    elif count_fishermans > THRESHOLD_FISHERMANS_12:
        price_rent -= (price_rent *
                       PERCENT_DISCOUNT_25)

if count_fishermans % 2 == 0 and season != 'Autumn':
        price_rent -= (price_rent * ADDITIONAL_PERCENT_DISCOUNT_5)

if budjet >= price_rent:
     print(f'Yes! You have {budjet - price_rent:.2f} leva left.')
else:
     print(f'Not enough money! You need {price_rent - budjet:.2f} leva.')





