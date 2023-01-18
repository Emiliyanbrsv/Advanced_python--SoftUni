both_numbers = [int(x) for x in input().split()]
first_number, second_number = int(both_numbers[0]), int(both_numbers[1])
first_set = set()
second_set = set()

for num in range(first_number):
    current_number = int(input())
    first_set.add(current_number)
for _ in range(second_number):
    current_number = int(input())
    second_set.add(current_number)

repeated_number = first_set.intersection(second_set)
for repeated in repeated_number:
    print(repeated)
