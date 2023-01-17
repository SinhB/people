from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    id: int
    name: str
    age: int
    gender: str
    country: str


@dataclass()
class PersonForm:
    name: str
    age: int
    gender: str
    country: str
