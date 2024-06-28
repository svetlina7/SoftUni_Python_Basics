DECOR_PERCENT = 0.10
DISCOUNT_CLOTHING = 0.10
NEEDED_EXTRAS_FOR_DISCOUNT = 151

budjet = float(input())
count_extras = int(input())
price_clothing_one_extra = float(input())

decor_price = budjet*DECOR_PERCENT
clothing_sum = count_extras * price_clothing_one_extra

if count_extras >= NEEDED_EXTRAS_FOR_DISCOUNT:
    clothing_sum -= (clothing_sum * DISCOUNT_CLOTHING)

needed_sum_for_movie = decor_price + clothing_sum

if needed_sum_for_movie > budjet:
    print("Not enough money!")
    print (f"Wingard needs {needed_sum_for_movie - budjet:.2f} leva more.")
else:
    print("Action!")
    print (f'Wingard starts filming with {budjet - needed_sum_for_movie:.2f} leva left.')


