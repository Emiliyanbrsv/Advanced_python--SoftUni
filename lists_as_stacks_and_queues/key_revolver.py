from _collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence = int(input())
shoot_bullets = 0
total_barrel = barrel_size
while True:
    if len(locks) <= 0 or len(bullets) <= 0:
        break
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_lock >= current_bullet:
        print('Bang!')
    else:
        locks.appendleft(current_lock)
        print('Ping!')

    total_barrel -= 1
    shoot_bullets += 1
    if total_barrel <= 0:
        if bullets:
            print('Reloading!')
            total_barrel = barrel_size

cost_of_bullets = shoot_bullets * bullet_price
earned = intelligence - cost_of_bullets
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned}")
