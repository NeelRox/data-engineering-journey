import json


with open('python/day5/user1.json','r') as file:
    reader=json.load(file)


result1=[]

for row in reader:
    if row['age']>=18:
        result1.append(row)


result2=sorted(result1 ,key=lambda result1:result1['age'], reverse='True')

with open('python/day5/result1.json','w') as file:
    json.dump(result2,file,indent=2)
    
print(result2)
