MIN_POINTS = 1250.5

actor_name = input()
started_academy_points = float(input())
judjes_count = int(input())

result = ''

for _ in range(judjes_count):
    judje_name = input()
    judjes_points = float(input())

    started_academy_points +=len(judje_name) * judjes_points / 2

    if started_academy_points > MIN_POINTS:
        result =  f'Congratulations, {actor_name} got a nominee for leading role with {started_academy_points:.1f}!'
        break
else:
    result = f'Sorry, {actor_name} you need {MIN_POINTS - started_academy_points:.1f} more!'

print(result)



