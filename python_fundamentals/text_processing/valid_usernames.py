def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def only_allowed_characters(name):
    for char in name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def has_no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def is_valid(name):
    if valid_length(name) and only_allowed_characters(name) and has_no_redundant_symbols(name):
        return True
    return False


usernames = input().split(', ')
for username in usernames:
    if is_valid(username):
        print(username)
