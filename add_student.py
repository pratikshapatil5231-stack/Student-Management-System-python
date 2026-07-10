def add_student():
    student_name=input("Enter student name:")
    usn=input("Enter USN:")
    branch=input("Enter Branch:")
    semester=int(input("Enter Semester:"))
    python_marks=int(input("Enter Python marks:"))
    java_marks=int(input("Enter Java marks:"))
    dbms_marks=int(input("Enter DBMS marks:"))
    return student_name,usn,branch,semester,python_marks,java_marks,dbms_marks