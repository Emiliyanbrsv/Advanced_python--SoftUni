from _collections import deque

firework = deque(int(x) for x in input().split(', '))
explosive = [int(x) for x in input().split(', ')]

fireworks_type = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

enough_firework = False

while firework and explosive:
    if firework[0] <= 0:
        firework.popleft()
        continue
    if explosive[-1] <= 0:
        explosive.pop()
        continue

    curr_firework = firework.popleft()
    curr_explosive = explosive.pop()
    sum_value = curr_explosive + curr_firework

    if sum_value % 3 == 0 and sum_value % 5 != 0:
        fireworks_type['Palm Fireworks'] += 1
    elif sum_value % 5 == 0 and sum_value % 3 != 0:
        fireworks_type['Willow Fireworks'] += 1
    elif sum_value % 15 == 0:
        fireworks_type['Crossette Fireworks'] += 1
    else:
        firework.append(curr_firework - 1)
        explosive.append(curr_explosive)

    if fireworks_type['Palm Fireworks'] >= 3 and fireworks_type['Willow Fireworks'] >= 3 and fireworks_type[
        'Crossette Fireworks'] >= 3:
        enough_firework = True
        print(f"Congrats! You made the perfect firework show!")
        break

if not enough_firework:
    print(f"Sorry. You can't make the perfect firework show.")

if firework:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework)}")
if explosive:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive)}")

for product, amount in fireworks_type.items():
    print(f"{product}: {amount}")
