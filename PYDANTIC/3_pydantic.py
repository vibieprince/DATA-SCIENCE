from pydantic import BaseModel, EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in between 50 characters',examples=['Amit','Nitish'])]
    # email: str 
    email: EmailStr
    linkedinurl: AnyUrl
    age: int = Field(gt=0,lt=120)
    weight: Annotated[float,Field(gt=0,strict=True)]  # matlab ab '75.2' kind of values bhi accept nhi hongi
    married: Annotated[bool,Field(description='Is the patient married or not')] 
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)] # Field ko optional banane ke liye usko ek default value deni hoti hai
    contact_details: Dict[str,str]


patient_info = {'name':'Nitish','email':'abc@gmail.com','linkedinurl':'https://www.linkedin.com/in/vibieprince','age':30,'weight':64.5,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890'}}

patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedinurl)
    print(patient.allergies)
    print('Inserted')

insert_patient_data(patient1)