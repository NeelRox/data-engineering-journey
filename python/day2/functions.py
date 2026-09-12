#exercise1

numbers=[10,20,30,40,50]

def calculate_avg(numbers):
    total=0
    count=0
    for num in  numbers:
        total+=num
        count+=1
    return total/count


avg_number=calculate_avg(numbers)

print(avg_number)



#exercise2

users = [
    {"name": "Rahul", "age": 28},
    {"name": "Priya", "age": 17},
    {"name": "Amit", "age": 31}
]

def user_above_18(users):
    result=[]
    for user in users:
        if user['age']>=18:
            result.append(user)
    return result


user_name=user_above_18(users) 

print(user_name)



#excersise3

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

def transform_user(users):
    return{
        'user_id':users['id'],
        'name':users['name'],
        'city':users['city'],
        'age':users['age']
    }

transform_users=[]
for user in users:
    transform_users.append(transform_user(user))

print(transform_users)    






