from .file_handler import load_students, save_students

def delete_student():

    students = load_students()

    roll = input("Enter Roll Number: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            save_students(students)

            print("\n✅ Deleted Successfully!\n")

            return

    print("\n❌ Student Not Found!\n")