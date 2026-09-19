import csv
import psycopg2

result=[]

def  age_convert(age):
    try:
        return int(age)
    except (ValueError,TypeError) :
        return None

with open('python/day13/users.csv','r') as file:
    reader = csv.DictReader(file)




    for  row in reader:
        row['age']=age_convert(row['age'])
        if row['age'] is not None and row['age']>=18:
            result.append(row)


print("Transformed data:")
print(result)        

connection = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    database="postgres",
    user="postgres",
    password="Neel@14"
    )

cursor = connection.cursor()

print("PostgreSQL connected!")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_etl (
        id INTEGER Primary Key,
        name VARCHAR(100),
        age INTEGER,
        city VARCHAR(100)
    )
""")

connection.commit()

print("Table created!")

for row in result:

    cursor.execute(
        """
        INSERT INTO users_etl (id, name, age, city)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """,
        (
            int(row['id']),
            row['name'],
            row['age'],
            row['city']
        )
    )

connection.commit()

print("Data loaded successfully!")


cursor.close()
connection.close()



