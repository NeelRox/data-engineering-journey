
user=[]

def convert_age(age):
    try:
        return int(age)
    except ValueError:
        return None

def transform_user(row):
    row['id']=int(row['id'])
    row['age']=convert_age(row['age'])
    if row['age'] is  None:
        return None

    return {
        'user_id':row['id'],
        'age':row['age'],
        'city':row['city'],
        'name':row['name']

    }

