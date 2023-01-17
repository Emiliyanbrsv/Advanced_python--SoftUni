data = input()

stack = []
for char in data:
    stack.append(char)

while stack:
    print(stack.pop(),end='')