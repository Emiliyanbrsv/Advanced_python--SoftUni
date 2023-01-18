clothes = list(map(int, input().split()))
rack_capacity = int(input())
rack_counter = 0
current_rack = 0
while len(clothes) > 0:
    current_clothes = clothes.pop()
    current_rack += current_clothes
    if current_rack == rack_capacity:
        rack_counter += 1
        current_rack = 0
    elif current_rack > rack_capacity:
        rack_counter += 1
        clothes.append(current_clothes)
        current_rack = 0
if current_rack != 0:
    rack_counter += 1
print(rack_counter)
