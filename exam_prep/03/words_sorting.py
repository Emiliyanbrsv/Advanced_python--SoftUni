def words_sorting(*words):
    sum_of_values = 0
    words_dict = {}

    for word in words:
        words_dict[word] = 0
        for l in word:
            words_dict[word] += ord(l)
            sum_of_values += ord(l)

    result = []
    if sum_of_values % 2 == 0:
        sorted_dict = sorted(words_dict.items(), key=lambda x: x[0])

    else:
        sorted_dict = sorted(words_dict.items(), key=lambda x: -x[1])

    for word, sums in sorted_dict:
        result.append(f'{word} - {sums}')

    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
