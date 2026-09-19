import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="Neel@14"
)

cursor = connection.cursor()

cursor.execute("""
    SELECT id, name, age
    FROM students
    WHERE age > %s
""", (28,))

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
