import requests


response = requests.get("https://jsonplaceholder.typicode.com/users")

users=response.json()

for row in users:
    id=row.get('id')
    name=row.get('name')
    email=row.get('email')
    city=row['address']['city']

    print(id,'-',name,'-',email)


    print(f"{name} lives in {city}")


print(response.status_code)
