def password_validation(password):
    pass_is_valid = True
    if not 6 <= len(password) <= 10:
        pass_is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        pass_is_valid = False
        print("Password must consist only of letters and digits")
    numbers_count = 0
    for char in password:
        if char.isdigit():
            numbers_count += 1
    if numbers_count < 2:
        pass_is_valid = False
        print("Password must have at least 2 digits")
    return pass_is_valid


some_password = input()
password_is_valid = password_validation(some_password)
if password_is_valid:
    print("Password is valid")
