from collections import deque


def stock_availability(*args):
    stock = list(args)
    inventory = deque(stock.pop(0))
    command = stock.pop(0)
    if command == 'delivery':
        inventory.extend(stock)

    elif command == 'sell':
        if len(stock) > 0:
            for product in stock:
                while product in inventory:
                    inventory.remove(product)
            if stock[0] in range(1, 10):
                while int(stock[0]) > 0:
                    inventory.popleft()
                    stock[0] -= 1

        else:
            inventory.popleft()
    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
