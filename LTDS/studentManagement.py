students = []
subjects = ("Physics", "Chemistry", "Math")
student_details = {}
courses = set()

name = input("Enter student name: ")

students.append(name)

student_details[name] = {
    "Age": 20,
    "Department": "Science"
}
courses.add("Python")

print("Student Added Successfully")

name = input("Enter student name to remove: ")

if name in students:
    students.remove(name)
    del student_details[name]
    print("Student Removed")
else:
    print("Student Not Found")

name = input("Enter student name to search: ")

if name in students:
    print("Student Found")
    print(student_details[name])
else:
    print("Student Not Found")

print("Students List:")
for student in students:
    print(student)

print("Subjects:")
print(subjects)

print("Student Details:")
print(student_details)

print("Unique Courses:")
print(courses)