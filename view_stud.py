from .file_handler import load_students

def view_students():

    students = load_students()

    if not students:
        print("\n❌ No Students Found!\n")
        return

    print("\n====== STUDENT RECORDS ======\n")

    for student in students:

        print(f"Roll No : {student['roll']}")
        print(f"Name    : {student['name']}")
        print(f"Age     : {student['age']}")
        print(f"Course  : {student['course']}")
        print("----------------------------")