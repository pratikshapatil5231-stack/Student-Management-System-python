from add_student import add_student
from calculate_marks import calculate_marks
from grade import get_grade
from menu import menu

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
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n===== Student List =====")
            for student in students:
                print("---------------------------")
                print("Name:", student["student_name"])
                print("USN:", student["usn"])
                print("Branch:", student["branch"])
                print("Semester:", student["semester"])
                print("Python:", student["python_marks"])
                print("Java:", student["java_marks"])
                print("DBMS:", student["dbms_marks"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Grade:", student["grade"])

    elif choice == 3:
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["student_name"].lower() == search_name.lower():
                print("\n===== Student Found =====")
                print("Name:", student["student_name"])
                print("USN:", student["usn"])
                print("Branch:", student["branch"])
                print("Semester:", student["semester"])
                print("Python:", student["python_marks"])
                print("Java:", student["java_marks"])
                print("DBMS:", student["dbms_marks"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Grade:", student["grade"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 4:
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["student_name"].lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted successfully.")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")