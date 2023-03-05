def age_assignment(*args, **kwargs):
    args = sorted(args)
    name_age = {}

    for name in args:
        for key, value in kwargs.items():
            if name[0] == key:
                name_age[name] = value

    return '\n'.join(f"{k} is {v} years old." for k, v in name_age.items())


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
