import psycopg2



connection = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    database="postgres",
    user="postgres",
    password="Neel@14"
    )

cursor = connection.cursor()

cursor.execute("""
insert into students (name,age) values('Rox',28)
"""
)

connection.commit()

print("value inserted in table successfully")

cursor.close()
connection.close()
