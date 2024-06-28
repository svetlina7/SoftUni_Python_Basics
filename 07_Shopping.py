PERCENT_DISCOUNT = 0.15
PRICE_VIDEO_CARD = 250
PERCENT_PRICE_PROCESSOR = 0.35
PERCENT_PRICE_RAM = 0.10

budjet = float(input())
count_video_cards = int(input())
count_processors = int(input())
count_rams = int(input())

sum_video_cards = count_video_cards * PRICE_VIDEO_CARD
sum_processsors = count_processors * (PERCENT_PRICE_PROCESSOR * sum_video_cards)
sum_rams = count_rams * (sum_video_cards * PERCENT_PRICE_RAM)
sum_materials = sum_rams + sum_processsors + sum_video_cards

if count_video_cards > count_processors:
    sum_materials = sum_materials - (sum_materials * PERCENT_DISCOUNT)

if sum_materials > budjet:
    print(f'Not enough money! You need {sum_materials-budjet:.2f} leva more!')
else:
    print(f'You have {budjet - sum_materials:.2f} leva left!')
