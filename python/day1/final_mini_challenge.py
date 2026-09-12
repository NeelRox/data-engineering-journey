users = [
    {
        "id": 1,
        "name": "Rahul",
        "city": "Delhi",
        "age": 28
    },
    {
        "id": 2,
        "name": "Priya",
        "city": "Mumbai",
        "age": 22
    },
    {
        "id": 3,
        "name": "Amit",
        "city": "Delhi",
        "age": 31
    }
]



for user in users:
    print(user['name'],user['city'],user['age'])


for user in users:
    if user['city']=='Delhi' and user['age']>30:
        print(user['name'])

