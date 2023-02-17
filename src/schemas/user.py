from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    address: str
    age: int
    comment: str
    creation_date: datetime = datetime.utcnow()

    # def __init__(self, name, address, age, comment):
    #     self.name = name
    #     self.address = address
    #     self.age = age
    #     self.comment = comment
    #     self.creation_date = datetime.utcnow()


class UserResponse(BaseModel):
    name: str
    address: str
    age: int

    # def __init__(self, name, address, age, comment):
    #     self.name = name
    #     self.address = address
    #     self.age = age

    def __repr__(self):
        return f"The '{self.name}' user is {self.address} YO, live in {self.address} and is an USER!!!!!!"
