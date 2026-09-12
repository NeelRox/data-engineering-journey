
'''
users = [
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 31},
    {"name": "Amit", "age": 22}
]


result=[]

for user in users:
    user['person']=user.pop('name')
    if user['age']>22:
        result.append(user)

print(result)
'''
users = [
    {"name": "Rahul", "age": 25},
    {"name": "Priya", "age": 31},
    {"name": "Amit", "age": 22}
]


name_by_age=[user['name']:user['age'] for user in users]

print(name_by_age)
