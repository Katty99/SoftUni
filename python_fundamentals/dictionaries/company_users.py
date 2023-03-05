final = {}
while True:
    command = input()
    if command == 'End':
        break
    company_name, employee_id = command.split(" -> ")
    if company_name not in final.keys():
        final[company_name] = []
    if employee_id not in final[company_name]:
        final[company_name].append(employee_id)
for key, value in final.items():
    print(key)
    for id_n in final[key]:
        print(f"-- {id_n}")