import requests
import psycopg2
import os


def extract_user():

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)

        response.raise_for_status()

        users = response.json()

        return users


    except requests.exceptions.RequestException as error:
        print("API request failed",error)
        


def transform_users(users):
    user_list=[]
    for user in users:
        user_info={
            'id' : user['id'],
            'name': user['name'],
            'email': user['email'].lower(),
            'city':user['address']['city'],
            'company':user['company']['name']

        }

        user_list.append(user_info)
    return user_list    



connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

print("PostgreSQL connected!")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        city TEXT,
        company TEXT
    )
""")

connection.commit()


users = extract_user()

transformed_users = transform_users(users)

for user in transformed_users:
     cursor.execute(
            """
            INSERT INTO api_users (id, name, email, city, company)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (
                int(user['id']),
                user['name'],
                user['email'],
                user['city'],
                user['company']
            )
        )
    
connection.commit()
    
print("Data loaded successfully!")





print(transformed_users)

cursor.close()
connection.close()