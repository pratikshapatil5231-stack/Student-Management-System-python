from menu import menu
from add_student import add_student
from calculate_marks import calculate_marks
from grade import get_grade
from display_student import display_student
from search_student import search_student
from delete_student import delete_student

students = []

while True:
    choice = menu()

    if choice == 1:
        student_name, usn, branch, semester, python_marks, java_marks, dbms_marks = add_student()

        total, average = calculate_marks(python_marks, java_marks, dbms_marks)

        grade = get_grade(average)

        student = {
            "student_name": student_name,
            "usn": usn,
            "branch": branch,
            "semester": semester,
            "python_marks": python_marks,
            "java_marks": java_marks,
            "dbms_marks": dbms_marks,
            "total": total,
            "average": average,
            "grade": grade
        }

        students.append(student)
        print("\nStudent Added Successfully!")

    elif choice == 2:
        display_student(students)

    elif choice == 3:
        search_student(students)

    elif choice == 4:
        delete_student(students)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")