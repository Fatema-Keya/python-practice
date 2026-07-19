class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name} | Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person() 
        print(f"Profession: Teacher | Subject: {self.subject}")

class Student(Teacher):
    def __init__(self, name, age, subject, student_id):
        super().__init__(name, age, subject)
        self.student_id = student_id

    def display_student(self):
        self.display_teacher() 
        print(f"Role: Student | ID: {self.student_id}")

print("--- Teacher Data ---")
teacher1 = Teacher("Zonayed Sir", 40, "Python")
teacher1.display_teacher()

print("\n--- Student Data ---")
student1 = Student("Hamza", 22, "Computer Science", "S102")
student1.display_student()