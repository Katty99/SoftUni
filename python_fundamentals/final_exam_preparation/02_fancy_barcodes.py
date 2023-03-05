import re

number_of_barcodes = int(input())
for current in range(number_of_barcodes):
    barcode = input()
    pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
    result = re.findall(pattern, barcode)
    if result:
        valid = str(result)
        group = ''
        for i in range(len(valid)):
            if valid[i].isdigit():
                group += str(valid[i])
        if group:
            print(f'Product group: {group}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
