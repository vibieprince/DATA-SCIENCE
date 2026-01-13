from pydantic import BaseModel,EmailStr,field_validator,AnyUrl
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

    @field_validator('email')
    @classmethod
    def email_validator(cls,value): # cls se hum patient clsss ko access karwan rahe hain
        valid_domains = ['hdfc.com','icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1] # -1 matlab last ki chije chahiye as in gmail.com
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    # @field_validator('name') # abhi value type coercion ke baad mil rahi hai because of default mode = 'after'
    @field_validator('name',mode='before') # ab type coercion se pehle milegi
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after') #default is after
    @classmethod
    def validate_age(cls,value): # so agar age type coercion se pehle aayi too chances hain yahan error ayega 
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
    

patient_info = {'name':'Nitish','email':'abc@icici.com','linkedinurl':'https://www.linkedin.com/in/vibieprince','age':'30','weight':64.5,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'1234567890'}}

patient1 = Patient(**patient_info) # yahan pe hee type coercion hota hai

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.linkedinurl)
    print(patient.allergies)
    print('Inserted')

insert_patient_data(patient1)