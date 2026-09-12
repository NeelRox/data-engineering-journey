import csv
import json


user=[]

with open('python/day3/user.csv','r') as file:

    content = csv.DictReader(file)


    for row in content:
        row['id']=int(row['id'])
        row['age']=int(row['age'])
        user.append(row)   

adult=[]

for users in user:
    if users['age']>=18:
        adult.append(users)


with open('python/day3/adult.json','w') as file:
    json.dump(adult,file,indent=2)        

    
