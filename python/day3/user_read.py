import csv

with open('python/day3/user.csv','r') as file:
    content = csv.DictReader(file)

    for row in content:
        print(row)
