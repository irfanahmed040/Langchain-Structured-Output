from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name': "ahmed", 'age':25}

print(new_person)