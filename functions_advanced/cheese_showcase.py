def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for product in sorted_dict:
        result.append(product[0])
        result.extend(sorted(product[1], reverse=True))
    return '\n'.join([str(el) for el in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
