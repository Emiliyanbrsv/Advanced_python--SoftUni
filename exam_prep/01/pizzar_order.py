from collections import deque

pizza_orders = deque(int(x) for x in input().split(', ') if int(x) > 0)
employees = [int(x) for x in input().split(', ')]

total_pizzas = 0

while pizza_orders and employees:

    pizza = pizza_orders.popleft()
    if pizza > 10:
        continue
    pizza_maker = employees.pop()

    if pizza <= pizza_maker:
        total_pizzas += pizza

    elif pizza > pizza_maker:
        total_pizzas += pizza_maker
        pizza_orders.appendleft(pizza-pizza_maker)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
