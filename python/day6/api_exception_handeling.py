import requests
import json

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    response.raise_for_status()
    users=response.json()

except requests.exceptions.RequestException as error:
    print('API request failed',error)    

count=0

for row in users:
    count+=1

print(count)    


