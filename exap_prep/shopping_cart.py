def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': []}
    result = ''
    products = ''
    
    for command in args:
        if command == 'Stop':
            break
        else:
            meals, product = command[0], command[1]
            if meals == 'Pizza' and product not in cart['Pizza'] and len(cart[meals]) < 4:
                cart[meals].append(product)
            elif meals == 'Soup' and product not in cart['Soup'] and len(cart[meals]) < 3:
                cart[meals].append(product)
            elif meals == 'Dessert' and product not in cart['Dessert'] and len(cart[meals]) < 2:
                cart[meals].append(product)
            products += product

    if len(products) < 1:
        return 'No products in the cart!'

    sorted_dict = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_dict:
        result += f'{key}:\n'
        for sorted_value in sorted(value):
            result += f" - {sorted_value}\n"
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
