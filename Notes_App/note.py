import os

filename = "notes.txt"


# Create Note
def create_note():
    note = input("Enter your note: ")

    with open(filename, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")


# Read Notes
def read_notes():
    if not os.path.exists(filename):
        print("No notes found!")
        return

    with open(filename, "r") as file:
        content = file.read()

    if content.strip() == "":
        print("No notes available.")
    else:
        print("\n------ Your Notes ------")
        print(content)


# Update Notes
def update_notes():
    if not os.path.exists(filename):
        print("No notes found!")
        return

    new_content = input("Enter new notes: ")

    with open(filename, "w") as file:
        file.write(new_content)

    print("Notes updated successfully!")


# Delete Notes
def delete_notes():
    if os.path.exists(filename):
        os.remove(filename)
        print("Notes deleted successfully!")
    else:
        print("No notes found!")


# Main Menu
while True:
    print("\n===== Notes App =====")
    print("1. Create Note")
    print("2. Read Notes")
    print("3. Update Notes")
    print("4. Delete Notes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_note()

    elif choice == "2":
        read_notes()

    elif choice == "3":
        update_notes()

    elif choice == "4":
        delete_notes()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")