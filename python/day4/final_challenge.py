
''''
import csv
import json


def convert_age(age):
    try:
        return int(age)
    except ValueError:
        return None

    
user=[]

def transform_user(row):
    row['id']=int(row['id'])
    row['age']=convert_age(row['age'])
    if row['age'] is  None:
        return None

    return user.append(row)

with open('python/day4/data.csv','r') as file:
    reader=csv.DictReader(file)



     for row in reader:   
        transform_user(row)
        

final_output=[]

for users in user:
    final_output.append(users)

with open('python/day4/final_outout.json','w') as file:
    json.dump(final_output,file,indent=2)


'''



import csv
import json


def convert_age(age):
    try:
        return int(age)
    except ValueError:
        return None

    
user=[]

def transform_user(row):
    row['id']=int(row['id'])
    row['age']=convert_age(row['age'])
    if row['age'] is  None:
        return None

    return row

with open('python/day4/data.csv','r') as file:
    reader=csv.DictReader(file)


    for row in reader:  
        transformed=transform_user(row)
        if transformed is not None:
            user.append(transformed)
        

with open('python/day4/user.json','w') as file:
    json.dump(user,file,indent=2)






   
    
      













   
    
      










