NEEDED_MONEY_FOR_BG_VACATION = 100
NEEDED_MONEY_FOR_BALCANS_VACATION = 1000
NEEDED_MONEY_FOR_EUROPE_VACATION = 1000

PERCENT_DISC_FOR_BG_SUMMER = 0.30
PERCENT_DISC_FOR_BG_WINTER = 0.70
PERCENT_DISC_FOR_BALCANS_SUMMER = 0.40
PERCENT_DISC_FOR_BALCANS_WINTER = 0.80
PERCENT_DISC_FOR_EUROPE_SUMMER = 0.90
PERCENT_DISC_FOR_EUROPE_WINTER = 0.90

destination = ''
type_vacation = ''
price = 0

budjet = float(input())
season = input()

if season == 'summer':

    if budjet <= NEEDED_MONEY_FOR_BG_VACATION:
        price += (budjet * PERCENT_DISC_FOR_BG_SUMMER)
        type_vacation = 'Camp'
        destination = 'Bulgaria'
    elif budjet <= NEEDED_MONEY_FOR_BALCANS_VACATION:
        price += (budjet * PERCENT_DISC_FOR_BALCANS_SUMMER)
        type_vacation = 'Camp'
        destination = 'Balkans'
    else:
        price += (budjet * PERCENT_DISC_FOR_EUROPE_SUMMER)
        type_vacation = 'Hotel'
        destination = 'Europe'

elif season == 'winter':
    if budjet <= NEEDED_MONEY_FOR_BG_VACATION:
        price += (budjet * PERCENT_DISC_FOR_BG_WINTER)
        type_vacation = 'Hotel'
        destination = 'Bulgaria'
    elif budjet <= NEEDED_MONEY_FOR_BALCANS_VACATION:
        price += (budjet * PERCENT_DISC_FOR_BALCANS_WINTER)
        type_vacation = 'Hotel'
        destination = 'Balkans'
    else:
        price += (budjet * PERCENT_DISC_FOR_EUROPE_WINTER)
        type_vacation = 'Hotel'
        destination = 'Europe'

print(f'Somewhere in {destination}')
print(f'{type_vacation} - {price:.2f}')