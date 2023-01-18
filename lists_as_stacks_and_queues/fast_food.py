from collections import deque

food = int(input())
numbers = list(map(int,input().split()))
number_deque = deque(numbers)
total_numbers = deque(numbers)

while number_deque:
    current_food = total_numbers.popleft()
    if food >= current_food:
        food -= current_food
        number_deque.popleft()
    else:
        break
    
print(max(numbers))

queue_as_string = [str(x) for x in number_deque]
if len(number_deque)>0:
    print(f"Orders left: {' '.join(queue_as_string)}")
else:
    print("Orders complete")
        