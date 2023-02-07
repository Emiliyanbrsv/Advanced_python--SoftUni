def negative_or_positive(data):
    positive = sum([int(x) for x in data if x > 0])
    negative = sum([int(x) for x in data if x < 0])

    print(negative)
    print(positive)

    if abs(negative) > positive:
        return "The negatives are stronger than the positives"
    return "The positives are stronger than the negatives"


numbers = list(map(int, input().split()))
print(negative_or_positive(numbers))