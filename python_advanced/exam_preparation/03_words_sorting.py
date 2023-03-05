def words_sorting(*args):
    words = {}
    for word in args:
        current_sum = 0
        for letter in word:
            current_sum += ord(letter)
        words[word] = current_sum

    if sum(words.values()) % 2 == 1:
        result = []
        for key, value in sorted(words.items(), key=lambda x: -x[1]):
            result.append(f"{key} - {value}")
        result = '\n'.join(result)
        return result

    elif sum(words.values()) % 2 == 0:
        result = []
        for key, value in sorted(words.items(), key=lambda x: x[0]):
            result.append(f"{key} - {value}")
        result = '\n'.join(result)
        return result


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))