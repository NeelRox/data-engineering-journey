import csv

sum=0
count=0

with open('python/day3/user.csv','r') as file:
    reader = csv.DictReader(file)


    for row in reader:
        row['age']=int(row['age'])
        sum+=row['age']
        count+=1

avg_age=sum/count

print(avg_age)

