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
    UPDATE students
    SET age = %s
    WHERE name = %s
    """,
    (31, "Amit")
)

connection.commit()

print("Student updated successfully!")

cursor.close()
connection.close()