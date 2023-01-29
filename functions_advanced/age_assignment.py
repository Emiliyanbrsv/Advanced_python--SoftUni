def age_assignment(*args,**kwargs):
    result = []
    for l, age in kwargs.items():
        for name in args:
            if name.startswith(l):
                result.append(f'{name} is {age} years old.')
    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))