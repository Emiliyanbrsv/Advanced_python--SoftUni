def even_odd_filter(**kwargs):
    for key in kwargs.items():
        if key[0] == 'odd':
            kwargs['odd'] = list(filter(lambda x: x % 2 != 0, key[1]))

        elif key[0] == 'even':
            kwargs['even'] = list(filter(lambda x: x % 2 == 0, key[1]))
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
