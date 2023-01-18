from collections import deque

names = input().split()
toss = int(input())
names_deque = deque(names)
while len(names_deque) > 1:

    for _ in range(toss -1):
        names_deque.append(names_deque.popleft())
    print(f"Removed {names_deque.popleft()}")

print(f"Last is {names_deque[0]}")