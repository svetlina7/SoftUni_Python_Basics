food = input()

if food == 'banana' or food == 'apple' or food == 'kiwi' or food == 'cherry' or food == 'lemon' or food == 'grapes':
    result = 'fruit'
elif food == 'tomato' or food == 'cucumber' or food == 'pepper' or food == 'carrot':
    result = 'vegetable'
else:
    result = 'unknown'

print(result)