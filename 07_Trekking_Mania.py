THRESHOLD_GROUP_MUSALA = 5
THRESHOLD_GROUP_MONBLAN = 12
THRESHOLD_GROUP_KILIMANJARO = 25
THRESHOLD_GROUP_K2 = 40

count_group = int(input())

count_musala = 0
count_monblan= 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0

for _ in range (count_group):
    count_group = int(input())

    if count_group <= THRESHOLD_GROUP_MUSALA:
        count_musala += count_group

    elif count_group <= THRESHOLD_GROUP_MONBLAN:
        count_monblan += count_group

    elif count_group <= THRESHOLD_GROUP_KILIMANJARO:
        count_kilimanjaro += count_group

    elif count_group <= THRESHOLD_GROUP_K2:
        count_k2+= count_group

    else:
        count_everest += count_group

count_people = count_musala + count_monblan + count_kilimanjaro + count_k2 + count_everest

print(f'{count_musala /count_people *100:.2f}%')
print(f'{count_monblan /count_people *100:.2f}%')
print(f'{count_kilimanjaro /count_people *100:.2f}%')
print(f'{count_k2 /count_people *100:.2f}%')
print(f'{count_everest /count_people *100:.2f}%')
