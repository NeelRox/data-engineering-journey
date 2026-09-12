
import json

with open('python/day5/user.json','r') as file:
    reader=json.load(file)

user=[]
unique_user=set()

def age_convert(age):
     try:
          return int(age)
     except (ValueError,TypeError):
          return None


for row in reader:
     row['age']=age_convert(row.get('age'))
     if row['age'] is None:
        continue
     name=row.get('name')
     if name not in unique_user:
          unique_user.add(name)
          user.append(row)
     


with open('python/day5/result.json','w') as file:
        json.dump(user,file,indent=2)    


print(user)  
         
             
