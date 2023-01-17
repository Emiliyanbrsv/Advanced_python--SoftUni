stack = []

while True:
    current_name = input()

    if current_name == 'End':
        print(f"{len(stack)} people remaining.")
        break

    elif current_name == "Paid":
        reversed_stack = []
        while stack:
            reversed_stack.append(stack.pop())
        while reversed_stack:
            print(reversed_stack.pop())

    else:
        stack.append(current_name)
