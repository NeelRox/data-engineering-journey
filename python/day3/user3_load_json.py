import json

with open('python/day3/user.json','r') as file:
    user=json.load(file)

print(user)  
print(user['name']) 
