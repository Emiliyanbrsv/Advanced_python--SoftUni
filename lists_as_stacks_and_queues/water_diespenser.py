from collections import deque
amount_of_water = int(input())

names_deque = deque()

while True:
    current_name = input()

    if current_name == 'Start':
        break
    
    names_deque.append(current_name)

while True:
    command = input()

    if command == 'End':
        print(f"{amount_of_water} liters left")
        break
    elif command.startswith('refill'):
        amount_of_water += int(command.split(' ')[1])
    else:
        person_name = names_deque.popleft()
        if int(command) <= amount_of_water:
            amount_of_water -= int(command)
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
