LITER_TO_ML = 1000

lenght = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume_fish_tank = lenght * width * height
volume_liters = volume_fish_tank / 1000
needed_liters = volume_liters * (1-percent)

print(needed_liters)