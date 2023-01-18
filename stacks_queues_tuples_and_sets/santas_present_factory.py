from _collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

present_dict = {
    150: ['Doll', 0],
    250: ['Wooden train', 0],
    300: ['Teddy bear', 0],
    400: ['Bicycle', 0]
}

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()

    if current_magic == 0 and current_material == 0:
        continue
    elif current_magic == 0:
        materials.append(current_material)
        continue
    elif current_material == 0:
        magic_level.appendleft(current_magic)
        continue

    multiplication = current_material * current_magic
    if multiplication < 0:
        value_of_sum = current_magic + current_material
        materials.append(value_of_sum)
    elif multiplication >= 0 and multiplication not in present_dict.keys():
        materials.append(current_material + 15)
    elif present_dict[multiplication]:
        present_dict[multiplication][1] += 1

doll = present_dict[150][1]
wooden_train = present_dict[250][1]
teddy_bear = present_dict[300][1]
bicycle = present_dict[400][1]

if (doll > 0 and wooden_train > 0) or (teddy_bear > 0 and bicycle > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for k, v in sorted(present_dict.items(), key=lambda x: x[1]):
    if v[1] > 0:
        print(f"{v[0]}: {v[1]}")
