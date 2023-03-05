import os


def file_traversal(path_name, first_level=False):
    for current_file in os.listdir(path_name):
        file = os.path.join(path_name, current_file)

        if os.path.isfile(file):
            extension = file.split('.')[-1]
            if extension not in extensions_dictionary:
                extensions_dictionary[extension] = []

            extensions_dictionary[extension].append(current_file)

        elif os.path.isdir(file) and not first_level:
            file_traversal(file, first_level=True)


directory = input()
extensions_dictionary = {}

file_traversal(directory)

dictionary = sorted(extensions_dictionary.items(), key=lambda x: x[0])
to_write = []

for extension, file_names in dictionary:
    to_write.append(f'.{extension}')

    for file in file_names:
        to_write.append(f"___{file}")

with open('files/report.txt', 'w') as file:
    file.write('\n'.join(to_write))