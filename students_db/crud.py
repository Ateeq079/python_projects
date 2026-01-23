# def create_student(cursor, conn, name, dept, gpa, grade):
#     cursor.execute(
#         "INSERT INTO std_info(name, dept, gpa, grade) VALUES (%s, %s, %s, %s);",
#         (name, dept, gpa, grade),
#     )
#     conn.commit()


# def read_student(cursor, st_id=None):
#     if st_id is None:
#         cursor.execute("SELECT * FROM std_info ORDER BY st_id;")
#     else:
#         cursor.execute("SELECT * FROM std_info WHERE st_id=%s;", (st_id,))
#     return cursor.fetchall()


# def update_student(cursor, conn, st_id, name, dept, gpa, grade):
#     cursor.execute(
#         """
# UPDATE std_info
# SET name=%s, dept=%s, gpa=%s, grade=%s
# WHERE st_id=%s;
# """,
# (name, dept, gpa, grade, st_id),
#     )
#     conn.commit()


# def delete_student(cursor, conn, st_id):
#     cursor.execute("DELETE FROM std_info WHERE st_id=%s;", (st_id,))
#     conn.commit()

import psycopg2, json

with open("config.json", "r") as file:
    config = json.load(file)

db_config = config["postgres"]


def get_db_connection():
    connection = psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )
    return connection


def execute_query(query, params=None, fetch=False):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(query, params or ())

    result = cursor.fetchall() if fetch else None
    affected_rows = cursor.rowcount

    conn.commit()
    cursor.close()
    conn.close()

    return result, affected_rows
