TRESHOLD_DEGREE_10 = 10
TRESHOLD_DEGREE_18 = 18
TRESHOLD_DEGREE_24 = 24
TRESHOLD_DEGREE_25 = 25

degrees = int(input())
type_for_the_day = input()

outfit = ''
shoes = ''

if type_for_the_day == 'Morning':
    if TRESHOLD_DEGREE_10 <= degrees <= TRESHOLD_DEGREE_18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif TRESHOLD_DEGREE_18 < degrees <= TRESHOLD_DEGREE_24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= TRESHOLD_DEGREE_25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif type_for_the_day == 'Afternoon':
    if TRESHOLD_DEGREE_10 <=degrees <= TRESHOLD_DEGREE_18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif TRESHOLD_DEGREE_18 < degrees <= TRESHOLD_DEGREE_24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= TRESHOLD_DEGREE_25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
else:
    if TRESHOLD_DEGREE_10 <= degrees <= TRESHOLD_DEGREE_18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif TRESHOLD_DEGREE_18 < degrees <= TRESHOLD_DEGREE_24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= TRESHOLD_DEGREE_25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
