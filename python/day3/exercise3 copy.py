import csv
import json


user=[]

with  open('python/day3/user.csv','r') as file :
    reader= csv.DictReader(file)

    for row in reader:
        row['age']=int(row['age'])
        user.append(row)


adult1=[]

for users in user:
    if users['age']>=18:
        adult1.append(users)

with open('python/day3/exercise3_output.json','w') as file:
    json.dump(adult1,file,indent=2)        

