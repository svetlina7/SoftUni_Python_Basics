PERCENT_SHOES = 0.40
PERCENT_TRAINING_TEAM = 0.20
PERCENT_BALL = 0.25
PERCENT_ACC = 0.20

annual_training_tax = int(input())

shoes = annual_training_tax - (annual_training_tax * PERCENT_SHOES)
training_team = shoes - (shoes * PERCENT_TRAINING_TEAM)
ball = training_team * PERCENT_BALL
acc = ball * PERCENT_ACC

total_sum = annual_training_tax + shoes + training_team + ball + acc

print(total_sum)