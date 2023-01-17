from dataclasses import asdict
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from people.domain.entities import PersonForm, Person as PersonEntity
from people.application.repositories.people import PeopleRepository
from people.models.people import Person as ORMPerson


def orm_to_person_entity_adapter(database_person: ORMPerson) -> PersonEntity:
    """
    This function adapts a ORMPerson object obtained from the database
    to a PersonEntity object, which can be used in the domain layer.
    """
    if not database_person:
        return None
    return PersonEntity(
        id=database_person.id,
        name=database_person.name,
        age=database_person.age,
        gender=database_person.gender,
        country=database_person.country,
    )


class SqlitePeopleRepository(PeopleRepository):
    """
    Repository implementation for interacting with
    SQLite database using SQLAlchemy.
    """

    def __init__(self, database_session: AsyncSession):
        self.database_session = database_session

    async def _fetch_data(self, lookup):
        return await self.database_session.execute(lookup)

    async def bulk_create(self, people: list[PersonForm]) -> list[PersonEntity]:
        people = [ORMPerson(**asdict(person)) for person in people]

        self.database_session.add_all(people)
        await self.database_session.flush()
        await self.database_session.commit()

        return [orm_to_person_entity_adapter(person) for person in people]

    async def get_average_age_by_country(self) -> list:
        lookup = (
            select([ORMPerson.country, func.avg(ORMPerson.age)])
            .group_by(ORMPerson.country)
            .select_from(ORMPerson)
        )

        results = await self._fetch_data(lookup)

        return results

    async def get_gender_repartition(self, country: str):
        lookup = select([ORMPerson.gender, func.count(ORMPerson.gender)])
        if country:
            lookup = lookup.where(ORMPerson.country == country)
        lookup = lookup.group_by(ORMPerson.gender).select_from(ORMPerson)

        results = await self._fetch_data(lookup)

        return results

    async def get_number_for_country(self):
        lookup = (
            select([ORMPerson.country, func.count(ORMPerson.id)])
            .group_by(ORMPerson.country)
            .select_from(ORMPerson)
        )

        results = await self._fetch_data(lookup)

        return results
