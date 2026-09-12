import csv


user=[]

def convert_age(age):
    try:
        return int(age)
    except ValueError:
        return None

with open('python/day4/data.csv','r') as file:
    reader=csv.DictReader(file)



    for row in reader:
        row['age']=convert_age(row['age'])
        user.append(row)

print(user)        


