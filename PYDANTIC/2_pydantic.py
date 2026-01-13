from pydantic import BaseModel

class Patient(BaseModel):
    # step 1
    name: str
    age: int

# patient_info = {'name':'nitish','age':'thirty'} # ispe code error dega 
patient_info = {'name':'nitish','age':'30'} # but ispe nhi
# patient_info = {'name':'nitish','age':30} # aur na hee ispe

# step 2
patient1 = Patient(**patient_info)

# step 3
def insert_patient_date(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted')

insert_patient_date(patient1)