import pytest
import pytest_asyncio

from statistics import mean
from itertools import groupby

from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from people.core.config import settings
from people.infrastructure.repositories.people import SqlitePeopleRepository
from people.models.people import Base, Person as ORMPerson

from tests.factories.person import PersonFormFactory


@pytest_asyncio.fixture
async def session():
    # Create an in-memory SQLite database for testing
    engine = create_async_engine(settings.SQLITE_TEST_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    session_factory = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession, autoflush=False
    )
    async with session_factory() as session:
        try:
            yield session
        finally:
            await session.close()


@pytest.mark.asyncio
async def test_bulk_create(session):
    # Initialisation
    people = PersonFormFactory.create_batch(size=10)
    repository = SqlitePeopleRepository(database_session=session)
    result = await repository.bulk_create(people)

    assert len(result) == 10

    # Check rows in db table
    query = select([func.count()]).select_from(ORMPerson)
    result = await session.execute(query)
    assert result.scalar() == 10


@pytest.mark.asyncio
async def test_get_average_age_by_country(session):
    # Initialisation
    people = PersonFormFactory.create_batch(size=10)
    repository = SqlitePeopleRepository(database_session=session)
    await repository.bulk_create(people)

    result = await repository.get_average_age_by_country()
    rows = result.fetchall()

    # Test average by country
    people_by_country = {}
    for person in people:
        if person.country in people_by_country:
            people_by_country[person.country] = mean(
                [people_by_country[person.country], person.age]
            )
        else:
            people_by_country[person.country] = person.age
    assert dict(rows) == people_by_country


@pytest.mark.asyncio
async def test_get_gender_repartition(session):
    # Initialisation
    people = PersonFormFactory.create_batch(size=10)
    repository = SqlitePeopleRepository(database_session=session)
    await repository.bulk_create(people)

    # Choose country query param
    selected_country = people[0].country
    result = await repository.get_gender_repartition(selected_country)
    rows = result.fetchall()

    # Test number of gender for this country
    assert len(rows) == len(
        set([person.gender for person in people if person.country == selected_country])
    )

    # Test gender repartition for this country
    people_in_country = [
        person for person in people if person.country == selected_country
    ]
    expected_gender_repartition = {
        gender: len(list(group))
        for gender, group in groupby(people_in_country, key=lambda x: x.gender)
    }
    assert dict(rows) == expected_gender_repartition


@pytest.mark.asyncio
async def test_get_number_for_country(session):
    # Initialisation
    people = PersonFormFactory.create_batch(size=10)
    repository = SqlitePeopleRepository(database_session=session)
    await repository.bulk_create(people)

    result = await repository.get_number_for_country()
    rows = result.fetchall()

    print(people)

    # Test number of differents country
    assert len(rows) == len(set([person.country for person in people]))

    # Test number of people for each country
    people_by_country = {}
    for person in people:
        if person.country in people_by_country:
            people_by_country[person.country] += 1
        else:
            people_by_country[person.country] = 1
    assert dict(rows) == people_by_country
