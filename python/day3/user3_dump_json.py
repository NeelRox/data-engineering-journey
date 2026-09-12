import json

user = {
    "id": 1,
    "name": "Rahul",
    "city": "Delhi",
    "age": 28
}


with open('python/day3/user.json','w') as file:
    json.dump(user,file,indent=2)
