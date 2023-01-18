text = input()
text_data = {}

for char in text:
    if char not in text_data:
        text_data[char] = 0
    text_data[char] += 1

for k, v in sorted(text_data.items()):
    print(f"{k}: {v} time/s")
