number_of_tabs = int(input())
salary = int(input())
for i in range(number_of_tabs):
    website_name = input()
    if website_name == 'Facebook':
        salary -= 150
    elif website_name == 'Instagram':
        salary -= 100
    elif website_name == 'Reddit':
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
