PRICE_FINE_FB = 150
PRICE_FINE_INST = 100
PRICE_FINE_RED = 50

open_tabs = int(input())
salary = int(input())

result = ''

for _ in range (open_tabs):
    website = input()

    if website == 'Facebook':
        salary -= PRICE_FINE_FB
    elif website == 'Instagram':
        salary -= PRICE_FINE_INST
    elif website == 'Reddit':
        salary -= PRICE_FINE_RED

    if salary <= 0:
        result = ('You have lost your salary.')
        break
else:
    result = salary

print(result)
