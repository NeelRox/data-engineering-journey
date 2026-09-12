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

def get_city_users(users, city):
    data=[]   
    for user in users:
      if user['city']==city:
           data.append(user)
    return data

delhi_users=get_city_users(users, 'Delhi')
mumbai_users=get_city_users(users, 'Mumbai')

print('delhi_users:',delhi_users)
print('mumbai_users:',mumbai_users)



    



