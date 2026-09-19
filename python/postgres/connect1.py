import psycopg2


connection = psycopg2.connect(
    host='localhost',
    port=5432,
    database='postgres',
    user='postgres',
    password='Neel@14'

)


cursor = connection.cursor()

cursor.execute(""" 
create table if not exists students (
id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
        )
  """)

connection.commit()

print("Table created sucessfully")

cursor.close()
connection.close()

