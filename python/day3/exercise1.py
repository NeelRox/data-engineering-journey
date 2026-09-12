import csv

with open('python/day3/user.csv','r') as file:

    context = csv.DictReader(file)


    for row in context:
        print(f"{row['name']} lives in {row['city']}")

