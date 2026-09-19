import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="Neel@14"
)

cursor = connection.cursor()

cursor.execute(
    """
    DELETE FROM students
    WHERE id = %s
    """,
    (4,)
)

connection.commit()

print("Student deleted successfully!")

cursor.close()
connection.close()