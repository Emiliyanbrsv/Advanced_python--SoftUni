def students_credits(*args):
    credits = {}
    credit_sum = 0
    result = []
    for course in args:
        course = course.split('-')
        name_course = course[0]
        credit = int(course[1]) * (int(course[3]) / int(course[2]))
        credit_sum += credit
        credits[name_course] = credit
    if credit_sum >= 240:
        result.append(f"Diyan gets a diploma with {credit_sum:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - credit_sum:.1f} credits more for a diploma.")

    sorted_dict = sorted(credits.items(), key=lambda x: -x[1])
    for name, grade in sorted_dict:
        result.append(f"{name} - {grade:.1f}")
    return '\n'.join(result)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
