def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for key, value in kwargs:
        result.append(key)
        value_list = sorted(value, reverse=True)
        result += value_list
    return '\n'.join(str(x) for x in result)


print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
