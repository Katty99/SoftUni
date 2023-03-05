import os


def add_songs(*songs):
    songs_dictionary = {}
    for song, lyrics in songs:
        if song not in songs_dictionary:
            songs_dictionary[song] = []
        songs_dictionary[song].extend(lyrics)

    final = []
    for key, value in songs_dictionary.items():
        final.append('- '+key)
        if value:
            final.extend(value)

    return os.linesep.join(final)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
