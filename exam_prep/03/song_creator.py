def add_songs(*args):
    result = {}
    for song, lyrics in args:
        if song not in result:
            result[song] = []
        for lyric in lyrics:
            result[song].append(lyric)

    final = ''
    for music, text in result.items():
        final += f"- {music}\n"
        for txt in text:
            final += f"{txt}\n"
    return final


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
