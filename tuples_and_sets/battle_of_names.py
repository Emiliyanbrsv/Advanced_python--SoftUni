iterations = int(input())
odd_set = set()
even_set = set()

for num in range(1, iterations + 1):
    sum_ascii_name = sum(ord(letter) for letter in input()) // num

    if sum_ascii_name % 2 != 0:
        odd_set.add(sum_ascii_name)
    else:
        even_set.add(sum_ascii_name)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
