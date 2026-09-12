
import csv

user=[]

with open('python/day4/data.csv','r') as file:
    reader=csv.DictReader(file)

    for row in reader:
        try:
            row['age']=int(row['age'])
            user.append(row) 
        except ValueError:
           # print('Invalid value')  
           age=None
            #continue 

    
print(user)        