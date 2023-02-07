from functools import reduce


def operate(*args):
    operator = args[0]
    numbers = args[1:]

    def add():
        return sum(numbers)

    def subtract():
        return reduce(lambda x, y: x - y, numbers)

    def multiply():
        return reduce(lambda x, y: x * y, numbers)

    def divide():
        return reduce(lambda x, y: x / y if y != 0 else None, numbers)

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
