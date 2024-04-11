students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


# sorts the students out alphabetically while using lambda (unnamed function) for students name
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
