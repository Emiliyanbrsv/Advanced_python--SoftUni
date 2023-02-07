def grocery_store(**kwargs):
    products = []
    sorted_dict = dict(sorted(kwargs.items(),key=lambda x: (-x[1], -len(x[0]), x[0])))
    for product, amount in sorted_dict.items():
        products.append(f'{product}: {amount}')
    return '\n'.join(products)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
