from pydantic import BaseModel,EmailStr,model_validator,AnyUrl
from typing import List,Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedinurl: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients above age 60 must have an emergency contact')
        return model
    
patient_info = {'name':'Nitish','email':'abc@gmail.com','linkedinurl':'https://www.linkedin.com/in/vibieprince','age':'30','weight':64.5,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890'}}

patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedinurl)
    print(patient.allergies)
    print('Inserted')

insert_patient_data(patient1)
