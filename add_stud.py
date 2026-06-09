from .file_handler import load_students, save_students

def add_stud():

    students = load_students()

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    stud = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(stud)

    save_students(students)

    print("\n✅ Student Added Successfully!\n")