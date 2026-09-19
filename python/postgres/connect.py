import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="Neel@14"
)

print("Connected to PostgreSQL!")

connection.close()
