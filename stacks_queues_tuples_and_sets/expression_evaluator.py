from functools import reduce

data = input().split()

idx = 0

operators = {
    '*': lambda i: reduce(lambda a, b: int(a) * int(b), data[:i]),
    '/': lambda i: reduce(lambda a, b: int(a) / int(b), data[:i]),
    '-': lambda i: reduce(lambda a, b: int(a) - int(b), data[:i]),
    '+': lambda i: reduce(lambda a, b: int(a) + int(b), data[:i])
}
while idx < len(data):
    char = data[idx]

    if char in '*/-+':
        data[0] = int(operators[char](idx))
        [data.pop(1) for _ in range(idx)]
        idx = 0

    idx += 1
print(*data)
