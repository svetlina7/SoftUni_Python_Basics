number_one = int(input())
number_two = int(input())
operator = input()

print_text = ''

if operator == '+':
    print_text = f'{number_one} + {number_two} = {number_one+number_two} {"- even" if (number_one + number_two) % 2 == 0 else "- odd"}'
elif operator == '-':
    print_text = f'{number_one} - {number_two} = {number_one - number_two} {"- even" if (number_one - number_two) % 2 == 0 else "- odd"}'
elif operator == '*':
    print_text = f'{number_one} * {number_two} = {number_one * number_two} {"- even" if (number_one * number_two) % 2 == 0 else "- odd"}'
elif number_two == 0:
    print_text= f'Cannot divide {number_one} by zero'
elif operator == '/':
    print_text= f'{number_one} / {number_two} = {number_one/number_two:.2f}'
else:
    print_text = f'{number_one} % {number_two} = {number_one % number_two}'

print(print_text)