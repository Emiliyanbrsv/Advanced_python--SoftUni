iterations = int(input())
unique_names = {input() for _ in range(iterations)}
print('\n'.join(unique_names))

# 2
# print('\n'.join({input() for _ in range(int(input()))}))

