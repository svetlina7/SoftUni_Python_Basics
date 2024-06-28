PRICE_DOG_FOOD = 2.50
PRICE_CAT_FOOD = 4

count_dog_food = int(input())
count_cat_food = int(input())

total_sum = float(count_dog_food * PRICE_DOG_FOOD) + float(count_cat_food * PRICE_CAT_FOOD)

print(f'{total_sum} lv.')

