def delete_student(students):
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