def shopping_list(budget, **kwargs):
    result = []

    if budget < 100:
        return 'You do not have enough budget.'

    for product, data in kwargs.items():
        value = float(data[0]) * int(data[1])
        if value <= budget and len(result) < 5:
            result.append(f'You bought {product} for {value:.2f} leva.')
            budget -= value

    return '\n'.join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
