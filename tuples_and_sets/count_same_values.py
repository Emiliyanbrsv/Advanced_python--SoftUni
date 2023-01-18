numbers = tuple([float(x) for x in input().split()])
same_value = {x:numbers.count(x) for x in numbers}

for k, v in same_value.items():
    print(f"{k} - {v} times")
