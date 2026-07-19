class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Your Id is: {self.id} Your name is: {self.name} Your salary is: {self.salary}")


employees = []

for i in range(5):
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")

    emp = Employee(id, name, salary)

    employees.append(emp)

for emp in employees:
    emp.display()