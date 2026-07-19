import json

while True:
    print("\n===== JSON Student Management =====")
    print("1. Read Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose: ")

    # Read
    if choice == "1":
        with open("student.json", "r") as file:
            data = json.load(file)

        print("\nStudents List:")
        for student in data:
            print(f"Name: {student['name']}, Age: {student['age']}")

    # Add
    elif choice == "2":
        with open("student.json", "r") as file:
            data = json.load(file)

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        data.append({
            "name": name,
            "age": age
        })

        with open("student.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Student Added Successfully!")

    # Update
    elif choice == "3":
        with open("student.json", "r") as file:
            data = json.load(file)

        name = input("Enter Student Name: ")

        found = False

        for student in data:
            if student["name"] == name:
                student["age"] = int(input("Enter New Age: "))
                found = True
                break

        if found:
            with open("student.json", "w") as file:
                json.dump(data, file, indent=4)

            print("✅ Student Updated Successfully!")
        else:
            print("❌ Student Not Found!")

    # Delete
    elif choice == "4":
        with open("student.json", "r") as file:
            data = json.load(file)

        name = input("Enter Student Name: ")

        new_data = []

        found = False

        for student in data:
            if student["name"] != name:
                new_data.append(student)
            else:
                found = True

        if found:
            with open("student.json", "w") as file:
                json.dump(new_data, file, indent=4)

            print("✅ Student Deleted Successfully!")
        else:
            print("❌ Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")