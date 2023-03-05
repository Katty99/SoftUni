class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_LEN = 4
valid_domains = ['com', 'bg', 'org', 'net']

while True:
    email_address = input()
    if email_address == 'End':
        break

    if '@' not in email_address:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email_address.split('@')[0]) <= MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    if '.' not in email_address:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if email_address.split('.')[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")
