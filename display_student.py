def display_student(students):
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