from _collections import deque

number_of_pumps = int(input())
pumps_deque = deque()

for _ in range(number_of_pumps):
    command = input().split()
    amount, km_to_pump = int(command[0]), int(command[1])
    pumps_deque.append([amount, km_to_pump])

for attempt in range(number_of_pumps):
    tank = 0
    fail = False
    for fuel, km in pumps_deque:
        tank += fuel - km
        if tank < 0:
            pumps_deque.append(pumps_deque.popleft())
            fail = True
            break

    if not fail:
        print(attempt)
        break
