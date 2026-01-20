import psycopg2


def main():

    conn = psycopg2.connect(
        host="localhost",
        dbname="student_db",
        user="postgres",
        password="1234",
        port=5432,
    )

    cursor = conn.cursor()

    def create(name, dept, gpa, grade):
        cursor.execute(
            "INSERT INTO std_info(name, dept, gpa, grade) VALUES(%s, %s, %s, %s );",
            (name, dept, gpa, grade),
        )
        conn.commit()

    def read(st_id):
        student = None
        if st_id >= 0:
            cursor.execute(
                "SELECT * FROM std_info WHERE st_id = %s ORDER BY st_id; ", (st_id,)
            )
            student = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM std_info;")
            student = cursor.fetchall()
        conn.commit()
        return student

    def update(st_id, name, dept, gpa, grade):
        cursor.execute(
            """
        UPDATE std_info
        SET name=%s, dept=%s, gpa=%s, grade=%s
        WHERE st_id=%s
    """,
            (name, dept, gpa, grade, st_id),
        )
        conn.commit()

    def delete(st_id):
        if st_id:
            cursor.execute("DELETE FROM std_info WHERE st_id=%s;", (st_id,))
            conn.commit()
        else:
            print("Student does not exist.")

    def print_students_table(students):
        print("-" * 72)
        print(f"{'ID':<5} {'Name':<15} {'Dept':<16} {'GPA':<10} {'Grade':<10}")
        print("-" * 72)
        for s in students:
            print(f"{s[0]:<5} {s[1]:<15} {s[2]:<16} {s[3]:<10} {s[4]:<10}")
        print("-" * 72)

    print("Welcome to Student Managment Program")
    print("Select an operation")

    while True:
        choice = int(
            input(
                " ---------\n1.Create a Student. \n2.Read a Student data. \n3.Update a Student data. \n4.Delete a Student data \n5.Exit \n -----------\n"
            )
        )
        if choice == 1:
            name = input("Enter student name:")
            dept = input("Enter dept:")
            gpa = input("Enter gpa:")
            grade = input("Enter grade:")

            create(name, dept, gpa, grade)

        elif choice == 2:
            st_data = None
            try:
                st_id = int(input("Enter student ID:"))
                st_data = read(st_id)
            except Exception as e:
                st_data = read(-1)
            print_students_table(st_data)

        elif choice == 3:
            st_id = int(input("Enter student ID:"))
            name = input("Enter student name")
            dept = input("Enter dept")
            gpa = input("Enter gpa")
            grade = input("Enter grade")
            update(st_id, name, dept, gpa, grade)

        elif choice == 4:
            st_id = int(input("Enter student ID:"))
            if delete(st_id):
                print("The student has been succesfully deleted")

        elif choice == 5:
            print("Closing")
            return False

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
