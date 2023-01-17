from sqlalchemy import Column, Integer, String
from people.core.database import Base


class Person(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String, index=True)
    country = Column(String, index=True)
