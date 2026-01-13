from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:int
class Patient(BaseModel):
    name: str
    gender: str
    age: int 
    address: Address # itself a complex type of data combined with different data types

address_dict = {'city':'Gurugram','state':'Haryana','pin':100240}

address1 = Address(**address_dict) #object

patient_dict = {'name':'Nitish','gender':'male','age':35,'address':address1}

patient1 = Patient(**patient_dict)

print(patient1.address.state)


print(patient1.name)

print(patient1.address.city)

print(patient1.address.pin)