import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/users")

users=response.json()

user_list=[]

for row in users:
    user_info = {
        'user_id':row.get('id'),
        'name':row.get('name'),
        'email':row.get('email'),
        'city':row['address']['city']
    }


    user_list.append(user_info)

print(response.status_code)

with open('python/day6/api_call3_output','w') as file:
    json.dump(user_list,file,indent=2)    
