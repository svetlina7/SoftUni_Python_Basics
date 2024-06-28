DELAY_IN_METERES = 15
DELAY_IN_SECONDS = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

delay_in_seconds = distance_in_meters // DELAY_IN_METERES * DELAY_IN_SECONDS
swimmer_record = distance_in_meters * time_in_seconds_for_one_meter + delay_in_seconds

if swimmer_record < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {swimmer_record:.2f} seconds.')
else:
    print(f"No, he failed! He was {abs(record_in_seconds-swimmer_record):.2f} seconds slower.")