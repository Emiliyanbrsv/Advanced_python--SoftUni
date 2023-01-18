longest_intersection = set()
iterations = int(input())

for _ in range(iterations):
    first_numbers, second_number = [x.split(',') for x in input().split("-")]

    first_range = set(x for x in range(int(first_numbers[0]), int(first_numbers[1]) + 1))
    second_range = set(x for x in range(int(second_number[0]), int(second_number[1]) + 1))

    interaction = first_range.intersection(second_range)
    if len(interaction) > len(longest_intersection):
        longest_intersection = interaction

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}]"
      f" with length {len(longest_intersection)}")
