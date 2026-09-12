users = [
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 31},
    {"name": "Amit", "age": 22},
    {"name": "Neha", "age": 28}
]


sorted_user=sorted(users,key=lambda user:user['age'],reverse=True)

print(sorted_user)
