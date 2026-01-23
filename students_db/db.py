import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="student_db",
        user="postgres",
        password="1234",
        port=5432,
    )
