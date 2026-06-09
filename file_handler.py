import json
from pathlib import Path

STUDENTS_FILE = Path(__file__).resolve().parents[1] / "data" / "students.json"


def load_students():
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    STUDENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STUDENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
