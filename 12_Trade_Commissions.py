city = input()
sales = float(input())

bonus = 0
is_input_valid = True

if city == 'Sofia':
    if 0 <= sales <= 500:
        bonus = 0.05
    elif 500 < sales <=1000:
        bonus = 0.07
    elif 1000 < sales <= 10000:
        bonus = 0.08
    elif sales > 10000:
        bonus = 0.12
    # else:
    #     is_input_valid = False

if city == 'Varna':
    if 0 <= sales <= 500:
        bonus = 0.045
    elif 500 < sales <= 1000:
        bonus = 0.075
    elif 1000 < sales <= 10000:
        bonus = 0.10
    elif  sales > 10000:
        bonus = 0.13
    # else:
    #     is_input_valid = False

if city == 'Plovdiv':
    if 0 <= sales <= 500:
        bonus = 0.055
    elif 500 < sales <= 1000:
        bonus = 0.08
    elif 1000 < sales <= 10000:
        bonus = 0.12
    elif sales > 10000:
        bonus = 0.145
#     else:
#         is_input_valid = False

else:
    is_input_valid = False

if sales < 0:
    is_input_valid = False

if bonus > 0:
    result = sales * bonus
    print(f'{result:.2f}')
else:
    print('error')
