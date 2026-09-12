import csv

user=[]

with open('python/day3/user.csv','r') as file:
    content = csv.DictReader(file)


    for row in content:
        row['id']=int(row['id'])
        row['age']=int(row['age'])

        user.append(row)


    print(user)    


