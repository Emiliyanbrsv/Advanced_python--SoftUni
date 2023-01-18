experssion = input()

indexes = []

for i in range(len(experssion)):

    if experssion[i] == '(':
        indexes.append(i)

    elif experssion[i] == ')':
        start_index = indexes.pop()
        print(experssion[start_index:i+1])

