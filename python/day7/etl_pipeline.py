import requests
import json

def fetch_user():
    user_list=[]

    try:
        response=requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
        response.raise_for_status()

        users=response.json()
        
    except requests.exceptions.RequestException as error:
        print("Api request failed",error)

    
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
    return user_list  

def transform(user_list):
     for user in user_list:
          user['user_id']=int(user['user_id'])
     return user_list   

result=fetch_user()
result=transform(result)



with open('python/day7/challenge_output','w') as file:
    json.dump(result,file,indent=2)   




     



               













                        


