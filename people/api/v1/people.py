from fastapi import APIRouter, Depends, Query

from people.schemas.people import (
    Person,
    PeopleListIn,
    PeopleListOut,
    AverageAge,
    GenderRepartition,
    NumberRepartition,
)
from people.domain.entities import PersonForm, Person as PersonEntity
from people.application.repositories.people import PeopleRepository
from people.api.dependencies import get_people_repository

router = APIRouter()


def person_entity_to_api_adapter(person: PersonEntity) -> Person:
    """
    This function adapts a PersonEntity object used in the domain layer
    to a Person object, which can be used in the API response.
    """
    return Person(
        id=person.id,
        name=person.name,
        age=person.age,
        gender=person.gender,
        country=person.country,
    )


@router.post("/people/")
async def bulk_create(
    people_data: PeopleListIn,
    people_repo: PeopleRepository = Depends(get_people_repository),
) -> PeopleListOut:
    """
    Create people from a list.
    This endpoint allows you to create multiple people at once.

    Parameters:
        people_data (PeopleListIn): A list of people to be created.

    Returns:
        PeopleListOut: A list of created people.
    """
    people_form = [PersonForm(**dict(person)) for person in people_data.people]
    created_people = await people_repo.bulk_create(people_form)

    return PeopleListOut(
        created_people=[
            person_entity_to_api_adapter(person) for person in created_people
        ]
    )


@router.get("/people/average/age")
async def get_average_age(
    people_repo: PeopleRepository = Depends(get_people_repository),
) -> list[AverageAge]:
    """
    Get the average age of people grouped by country.

    Returns:
        AverageAgeByCountry: A list of average ages by country.
    """
    avg_age_by_country = await people_repo.get_average_age_by_country()
    return [AverageAge(country=c, average_age=a) for c, a in avg_age_by_country]


@router.get("/people/gender/")
async def get_gender_repartition(
    country: str = Query(None),
    people_repo: PeopleRepository = Depends(get_people_repository),
) -> list[GenderRepartition]:
    """
    Get the gender repartition for people in a given country.

    Parameters:
        country (str): The country for which to get the gender repartition.

    Returns:
        GenderRepartition: A list of gender repartition for the given country.
    """
    gender_repartition = await people_repo.get_gender_repartition(country)
    return [GenderRepartition(gender=g, count=c) for g, c in gender_repartition]


@router.get("/people/number")
async def get_number_of_people(
    people_repo: PeopleRepository = Depends(get_people_repository),
) -> list[NumberRepartition]:
    """
    Get the number of people grouped by country.

    Returns:
        NumberRepartition: A list of number repartition by country.
    """
    number_repartition = await people_repo.get_number_for_country()
    return [NumberRepartition(country=c, count=p) for c, p in number_repartition]
