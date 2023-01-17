iterations = int(input())
car_numbers = set()
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'

for _ in range(iterations):
    command, number = input().split(', ')

    if command == COMMAND_IN:
        car_numbers.add(number)
    elif command == COMMAND_OUT:
        car_numbers.remove(number)

if car_numbers:
    print('\n'.join(car_numbers))
else:
    print("Parking Lot is Empty")
