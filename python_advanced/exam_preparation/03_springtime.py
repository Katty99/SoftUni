import os


def start_spring(**kwargs):
    objects = {}
    for value, key in kwargs.items():
        if key not in objects:
            objects[key] = []
        objects[key].append(value)

    result = []
    for key, value in sorted(objects.items(),key=lambda x: (-len(x[1]), x[0])):
        result.append(key + ':')
        for val in sorted(value):
            result.append('-' + val)

    return os.linesep.join(result)


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))

# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))