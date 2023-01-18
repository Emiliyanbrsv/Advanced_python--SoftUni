from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cup_of_milks = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocolates and cup_of_milks:
    chocolate = chocolates.pop()
    cup_of_milk = cup_of_milks.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cup_of_milks.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
        continue
    else:
        chocolates.append(chocolate - 5)
        cup_of_milks.append(cup_of_milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f'Chocolate: {", ".join(str(x) for x in chocolates) if chocolates else "empty"}')
print(f'Milk: {", ".join(str(x) for x in cup_of_milks) if cup_of_milks else "empty"}')
