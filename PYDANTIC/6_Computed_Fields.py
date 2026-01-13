from pydantic import BaseModel,EmailStr,model_validator,AnyUrl,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedinurl: AnyUrl
    age: int
    weight: float
    height:float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
patient_info = {'name':'Nitish','email':'abc@gmail.com','linkedinurl':'https://www.linkedin.com/in/vibieprince','age':'30','weight':64.5,'height':1.72,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890'}}

patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedinurl)
    print("BMI",patient.bmi)
    print(patient.allergies)
    print('Inserted')

insert_patient_data(patient1)