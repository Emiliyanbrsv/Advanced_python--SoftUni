from collections import deque

seats = input().split(', ')
first_numbers = deque(int(x) for x in input().split(', '))
second_numbers = deque(int(x) for x in input().split(', '))

seat_matches = []
rotations = 0

while rotations < 10 and len(seat_matches) < 3:

    curr_first_number = first_numbers.popleft()
    curr_second_number = second_numbers.pop()
    numbers_sum = curr_first_number + curr_second_number
    first_seat_combination = str(curr_first_number) + chr(numbers_sum)
    second_seat_combination = str(curr_second_number) + chr(numbers_sum)
    rotations +=1

    if first_seat_combination in seats and first_seat_combination not in seat_matches:
        seat_matches.append(first_seat_combination)
    elif second_seat_combination in seats and second_seat_combination not in seat_matches:
        seat_matches.append(second_seat_combination)
    else:
        first_numbers.append(curr_first_number)
        second_numbers.appendleft(curr_second_number)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
