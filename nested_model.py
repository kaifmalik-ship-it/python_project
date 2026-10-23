from pydantic import BaseModel

class Address(BaseModel):

    city:str
    state:str
    pin:str 





class patient(BaseModel):
    name :str
    gender:str
    age: int
 

patient_dict={"name":"kaif","gender":"male","age":"22","address":Address}

patient_1=patient(**patient_dict)




print(patient_1.name)
print(patient_1.age)
