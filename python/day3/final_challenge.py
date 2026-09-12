import csv
import json


user=[]

with  open('python/day3/user.csv','r') as file :
    reader= csv.DictReader(file)

    for row in reader:
        row['user_id']=row.pop('id')
        row['user_id']=int(row['user_id'])
        row['age']=int(row['age'])
        if row['city']=='Delhi':
            user.append(row)

      
keys=['user_id','name','age']

final_output=[]

for users in user:
    new_dict={k: users[k] for k in keys}
    final_output.append(new_dict)



with open('python/day3/final_chellange_output.json','w') as file:
    json.dump(final_output,file,indent=2)     



