from _collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])
stamat_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    curr_milligram = milligrams_of_caffeine.pop()
    curr_drink = energy_drinks.popleft()

    if (curr_drink * curr_milligram)+stamat_caffeine <= 300:
        stamat_caffeine += (curr_drink * curr_milligram)
    else:
        energy_drinks.append(curr_drink)
        if stamat_caffeine - 30 >= 0:
            stamat_caffeine -= 30


if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
