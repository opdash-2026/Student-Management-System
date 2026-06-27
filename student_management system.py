students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")

    students.append({
        "Name": name,
        "Roll": roll,
        "Branch": branch
    })

    print("Student Added Successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    for student in students:
        print("------------------------")
        print("Name :", student["Name"])
        print("Roll :", student["Roll"])
        print("Branch :", student["Branch"])


def search_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["Roll"] == roll:
            print(student)
            return

    print("Student Not Found")


def delete_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Deleted Successfully")
            return

    print("Student Not Found")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
