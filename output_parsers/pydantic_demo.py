from pydantic import BaseModel,EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name:str ="devendra"
    age: Optional[int] = None
    email:EmailStr
    cgpa: float =Field(ge=0,le=10,description="Cgpa of the student between the range 0.0 to 10.0")


new_student = {'age':'32','email':'abc@adypu.edu.in','cgpa':10}


student = Student(**new_student)
print(student)
print(type(student))
