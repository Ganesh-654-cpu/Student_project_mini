from .file_handler import load_students

def search_student():

    students = load_students()

    roll = input("Enter Roll Number: ")

    for student in students:

        if student["roll"] == roll:

            print("\n✅ Student Found!\n")

            print(student)

            return

    print("\n❌ Student Not Found!\n")