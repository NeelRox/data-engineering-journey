import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="Neel@14"
)

cursor = connection.cursor()

name = "Amit"
age = 30

cursor.execute(
    """
    INSERT INTO students (name, age)
    VALUES (%s, %s)
    """,
    (name, age)
)

connection.commit()

print("Value inserted successfully!")

cursor.close()
connection.close()
