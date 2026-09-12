import requests
import json

try:
    response=requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    response.raise_for_status()

    users=response.json()

except requests.exceptions.RequestException as error:
    print("API request failed",error)

user_list=[]

for row in users:
    user_info={
        'user_id':row.get('id'),
        'name':row.get('name'),
        'email':row.get('email'),
        'city':row['address']['city']
    }
    if row['address']['city']=='South Christy':
        user_list.append(user_info)


print(response.status_code)

with open('python/day6/challenge_output','w') as file:
    json.dump(user_list,file,indent=2)       
        

