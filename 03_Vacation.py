MAX_SPENDING_DAYS = 5

needed_money_for_vacation = float(input())
balance = float(input())

total_count_days = 0
count_spending_days = 0
result = ''

while count_spending_days < MAX_SPENDING_DAYS:
    action = input()
    money = float(input())

    total_count_days += 1

    if action == 'spend':
        count_spending_days += 1
        balance = balance - money if balance > money else 0

    elif action == 'save':
        count_spending_days = 0
        balance += money

    if balance >= needed_money_for_vacation:
            result = f"You saved the money for {total_count_days} days."
            break

    else:
            result = f"You can't save the money.\n{total_count_days}"

print(result)

