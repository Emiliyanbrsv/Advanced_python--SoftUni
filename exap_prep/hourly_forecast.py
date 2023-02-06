def forecast(*args):
    result = []
    key_words = ['Sunny', 'Cloudy', 'Rainy']

    sorted_forecast = sorted(args,key=lambda x: (key_words.index(x[1]), x[0]))
    for city, weather in sorted_forecast:
        result.append(f"{city} - {weather}")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))