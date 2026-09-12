import requests
import json

response=requests.get("https://jsonplaceholder.typicode.com/users")



with open('python/day6/api_call_ouitput','w') as file:
    json.dump(response.json(),file,indent=2)

print(response.status_code)

print(response.json())




