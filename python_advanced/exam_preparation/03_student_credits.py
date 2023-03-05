def students_credits(*args):
    total_credits = 0
    final_dictionary = {}
    for arg in args:
        course_name, credit, max_points, points = arg.split('-')
        current_credits = int(points) * int(credit) / int(max_points)
        total_credits += current_credits
        final_dictionary[course_name] = current_credits

    result = []
    final_dictionary = sorted(final_dictionary.items(), key=lambda x: -x[1])
    for key, value in final_dictionary:
        result.append(f"{key} - {value:.1f}")
    result = '\n'.join(result)

    if total_credits >= 240:
        return f"Diyan gets a diploma with {total_credits:.1f} credits.\n{result}"
    else:
        return f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n{result}"


# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)