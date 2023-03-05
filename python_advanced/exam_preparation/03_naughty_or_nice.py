def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_or_naughty = {'Nice': [], 'Naughty': []}
    for data in args:
        nums = [x[0] for x in santa_list]
        number, status = data.split('-')
        number = int(number)
        if nums.count(number) == 1:
            for kid_num, kid_name in santa_list:
                if kid_num == number:
                    nice_or_naughty[status].append(kid_name)
                    santa_list.remove((kid_num, kid_name))
                    break

    for name, stat in kwargs.items():
        names = [x[1] for x in santa_list]
        if names.count(name) == 1:
            for kid_num, kid_name in santa_list:
                if name == kid_name:
                    nice_or_naughty[stat].append(name)
                    santa_list.remove((kid_num, kid_name))
                    break

    nice_or_naughty['Not found'] = [x[1] for x in santa_list]
    to_print = ''
    for key, value in nice_or_naughty.items():
        if value:
            to_print += f"{key}: {', '.join(value)}\n"

    return to_print.strip()


# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))