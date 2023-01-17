from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    age: int
    gender: str
    country: str

    class Config:
        orm_mode = True


class Person(PersonBase):
    id: int


class PeopleListIn(BaseModel):
    people: list[PersonBase]


class PeopleListOut(BaseModel):
    created_people: list[Person]


class AverageAge(BaseModel):
    country: str
    average_age: int


class GenderRepartition(BaseModel):
    gender: str
    count: int


class NumberRepartition(BaseModel):
    country: str
    count: int
