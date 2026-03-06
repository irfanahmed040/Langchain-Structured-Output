from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name:str = 'irfan'
    age :Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10)

new_student = {'age': 25, 'email':"abc@tericsoft.com", 'cgpa': 6.4}

student = Student(**new_student)

print(student)#doesnot print dictionary but a pydantic object

student_dict = dict(student) #convert pydantic object to dictionary

print(student_dict['email']) # now we can access the dictionary values using the keys

student_json = student.model_dump_json()

print(student_json)