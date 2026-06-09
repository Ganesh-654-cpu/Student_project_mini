from .file_handler import load_students, save_students

def update_student():

    students = load_students()

    roll = input("Enter Roll Number: ")

    for student in students:

        if student["roll"] == roll:

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            save_students(students)

            print("\n✅ Updated Successfully!\n")

            return

    print("\n❌ Student Not Found!\n")