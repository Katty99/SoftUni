name = input()
password = input()
password_entered = input()
while password_entered != password:
    password_entered = input()
else:
    print(f'Welcome {name}!')
