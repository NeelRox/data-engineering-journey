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

#challenge1

for user in users:
    if user['age']>=25:
        print(user['name'])

#challenge2

count=0

for user in users:    
    if user['city']=='Delhi':
        count=count+1
print(count)    

#challenge3

sum=0
count=0
for user in users:
    sum += user['age']
    count +=1

avg_age=sum/count
print(avg_age)  

    


