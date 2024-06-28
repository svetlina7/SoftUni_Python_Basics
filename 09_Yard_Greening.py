ONE_SQUARE_METER_WITH_VAT = 7.61
PERCENT_DISCOUNT = 18/100

landscaped_square_meters = float(input())

total_sum_without_disc = ONE_SQUARE_METER_WITH_VAT * landscaped_square_meters

total_sum_with_disc = total_sum_without_disc - (total_sum_without_disc * PERCENT_DISCOUNT)

sum_of_discount = total_sum_without_disc - total_sum_with_disc

print(f'The final price is: {total_sum_with_disc} lv.')
print(f'The discount is: {sum_of_discount} lv.')