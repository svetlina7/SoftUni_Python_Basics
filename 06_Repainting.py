PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINING = 5
PRICE_BAG= 0.40
ADITIONALLY_PAINT = 0.10
ADITIONALLY_NYLON = 2
WORKER_PRICE_PER_HOUR = 0.30

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thining = int(input())
work_hours = int(input())

quantity_nylon += ADITIONALLY_NYLON
quantity_paint += (quantity_paint * ADITIONALLY_PAINT)

total_sum_material = (quantity_nylon * PRICE_NYLON) \
                     + (quantity_paint * PRICE_PAINT) \
                     + (quantity_thining * PRICE_THINING) \
                     + PRICE_BAG

total_sum_repairs = (total_sum_material * WORKER_PRICE_PER_HOUR) * work_hours

total_sum = total_sum_material + total_sum_repairs

print(total_sum)