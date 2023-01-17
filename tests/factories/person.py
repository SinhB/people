import factory
from factory import Faker

from people.domain.entities import PersonForm, Person as PersonEntity
from people.models.people import Person as ORMPerson


class BasePersonFactory(factory.Factory):
    name = Faker("name")
    age = Faker("random_int", min=1, max=100)
    gender = Faker("random_element", elements=["male", "female", "neutral"])
    country = Faker("country_code")


class PersonFactory(BasePersonFactory):
    class Meta:
        model = PersonEntity


class ORMPersonFactory(BasePersonFactory):
    class Meta:
        model = ORMPerson


class PersonFormFactory(BasePersonFactory):
    class Meta:
        model = PersonForm
