from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:int
class Patient(BaseModel):
    name: str
    gender: str
    age: int 
    address: Address

address_dict = {'city':'Gurugram','state':'Haryana','pin':100240}

address1 = Address(**address_dict) #object

patient_dict = {'name':'Nitish','gender':'male','age':35,'address':address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump() # converts model into python dictionary
temp = patient1.model_dump_json() # converts model into json
# temp = patient1.model_dump(include=['name','gender'])
# temp = patient1.model_dump(exclude=['name','gender'])
temp = patient1.model_dump(exclude={'address':['state']})


temp = patient1.model_dump(exclude_unset=True) # jaise kuch values jo init nhi hui i.e optional thi unko exclude kardo

print(temp)
print(type(temp))
