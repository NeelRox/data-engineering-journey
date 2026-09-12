import json


with open('python/day5/user.json','r') as file:
    reader=json.load(file)

users=[]
duplicate_users=set()

def convert_age(age):
    try:
        return int(age)
    except (ValueError, TypeError):
        return None


for row in reader:
    row['age']=convert_age(row['age'])
    if row['age'] is None: 
        continue
    name=row.get('name')
    if row['age']>=18:
        if name not in duplicate_users:

            duplicate_users.add(name)
            users.append(row)


result=sorted(users,key=lambda user:user['age'], reverse=True)


with  open('python/day5/final_result.json','w') as file:
    json.dump(result,file,indent=2)

print(result)
    



