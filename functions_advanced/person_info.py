def get_info(**kwargs):
    data = []
    for value in kwargs.values():
        data.append(value)
    return f"This is {data[0]} from {data[1]} and he is {data[2]} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
