from _collections import deque

bowls_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls_ramen and customers:
    current_bowl = bowls_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        bowls_ramen.append(current_bowl-current_customer)

    elif current_customer > current_bowl:
        customers.appendleft(current_customer-current_bowl)

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")
elif len(bowls_ramen) == 0:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
