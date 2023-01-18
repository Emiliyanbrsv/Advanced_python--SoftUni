number_of_students = int(input())
student_data = {}

for _ in range(number_of_students):
    name, grade = input().split()

    if name not in student_data:
        student_data[name] = []
    student_data[name].append(float(grade))

for k, v in student_data.items():
    average_grade = sum(v) / len(v)
    print(f"{k} -> {' '.join(f'{x:.2f}' for x in v)} (avg: {average_grade:.2f})")
