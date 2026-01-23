from db import get_connection
from crud import (
    create_student,
    read_student,
    update_student,
    delete_student,
)


def show_menu():
    print(
        """
---------
1. Create a Student
2. Read Student data
3. Update Student data
4. Delete Student data
5. Exit
---------
"""
    )


def get_choice():
    return int(input("Enter your choice: "))


def print_students_table(students):
    print("-" * 72)
    print(f"{'ID':<5} {'Name':<15} {'Dept':<16} {'GPA':<10} {'Grade':<10}")
    print("-" * 72)
    for s in students:
        print(f"{s[0]:<5} {s[1]:<15} {s[2]:<16} {s[3]:<10} {s[4]:<10}")
    print("-" * 72)


def main():
    conn = get_connection()
    cursor = conn.cursor()

    print("Welcome to Student Management Program")

    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            name = input("Enter student name: ")
            dept = input("Enter dept: ")
            gpa = input("Enter gpa: ")
            grade = input("Enter grade: ")
            create_student(cursor, conn, name, dept, gpa, grade)

        elif choice == 2:
            try:
                st_id = int(input("Enter student ID (or press Enter for all): "))
                students = read_student(cursor, st_id)
            except:
                students = read_student(cursor)
            print_students_table(students)

        elif choice == 3:
            st_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            dept = input("Enter dept: ")
            gpa = input("Enter gpa: ")
            grade = input("Enter grade: ")
            update_student(cursor, conn, st_id, name, dept, gpa, grade)

        elif choice == 4:
            st_id = int(input("Enter student ID: "))
            delete_student(cursor, conn, st_id)
            print("Student deleted successfully")

        elif choice == 5:
            print("Closing program")
            break

        else:
            print("Invalid choice")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
