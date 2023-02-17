size = 6
matrix = [[line for line in input().split()] for _ in range(size)]

throw_counter = 0
points = 0

while throw_counter < 3:
    coordinates = input().strip('(')
    coordinates = coordinates.strip(')').split(',')
    r = int(coordinates[0])
    c = int(coordinates[1])
    throw_counter += 1
    if 0 <= r < size and 0 <= c < size:

        if matrix[r][c] == 'B':
            matrix[r][c] = '0'
            for index in range(size):
                number = matrix[index][c]
                if number.isdigit():
                    points += int(number)

if 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won {'Football'}.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won {'Teddy Bear'}.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won {'Lego Construction Set'}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
    