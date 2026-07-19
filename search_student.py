def search_student(students):
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