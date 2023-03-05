def concatenate(*args, **kwargs):
    phrase = ''.join(args)

    for key, value in kwargs.items():
        if key in phrase:
            phrase = phrase.replace(key, value)

    return phrase


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
