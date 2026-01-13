# def insert_patient_data(name,age):
#     print(name)
#     print(age)
#     print('Inserted into database')

def insert_patient_data(name:str,age:int):
    if type(name) == str and type(age)==int:
        print(name)
        print(age)
        print('Inserted into database')
    else:
        raise TypeError('Incorrect data type')

def update_patient_data(name:str,age:int):
    if type(name) == str and type(age)==int:
        print(name)
        print(age)
        print('updated into database')
    else:
        raise TypeError('Incorrect data type')

# kitne function banaoge aur kitni if statements lagaoge
# agar variables ko ek particular range chaiye for example age not neagtive wo kese handle hoga?
# so use pydanticyd