itterations = int(input())

numbers_stack = []

for _ in range(itterations):
    command = input()

    if command.startswith('1'):
        command = command.split()
        current_number = int(command[1])
        numbers_stack.append(current_number)
    elif numbers_stack:
        if command == '2':
            numbers_stack.pop()
        elif command == '3':
            print(max(numbers_stack))
        elif command == '4':
            print(min(numbers_stack))

reversed_number_stack = []
while numbers_stack:
    reversed_number_stack.append(str(numbers_stack.pop()))
print(', '.join(reversed_number_stack))

