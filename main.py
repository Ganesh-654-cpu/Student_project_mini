
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from modules import add_stud
from modules import view_stud
from modules import search_stud
from modules import update_stud
from modules import delete_stud


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_stud()

    elif choice == "2":
        view_stud()

    elif choice == "3":
        search_stud()

    elif choice == "4":
        update_stud()

    elif choice == "5":
        delete_stud()

    elif choice == "6":
        print("\nThank You!\n")
        break

    else:
        print("\n Invalid Choice!\n")