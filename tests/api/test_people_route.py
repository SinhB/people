from unittest.mock import patch
from starlette.testclient import TestClient

from people.main import app
from people.infrastructure.repositories.people import SqlitePeopleRepository
from people.domain.entities import Person as PersonEntity
from people.schemas.people import PeopleListOut, Person

client = TestClient(app)


def test_bulk_create_validation_error():
    """
    Test that the bulk create endpoint returns
    a validation error if required fields are missing.
    """
    people_data = {
        "people": [
            {"name": "John Doe", "age": 30, "gender": "male", "country": "US"},
            {"name": "Jane Doe", "age": 25, "gender": "female"},
        ]
    }

    response = client.post("/v1/people/", json=people_data)
    assert response.status_code == 422


@patch.object(
    SqlitePeopleRepository,
    "bulk_create",
    return_value=PeopleListOut(
        created_people=[
            PersonEntity(id=1, name="John Doe", age=30, gender="male", country="US")
        ]
    ),
)
def test_bulk_create(mock_bulk_create):
    """
    Test that the bulk create endpoint creates people and returns the correct response.
    """
    people_data = {
        "people": [{"name": "John Doe", "age": 30, "gender": "male", "country": "US"}]
    }

    with patch(
        "people.api.v1.people.person_entity_to_api_adapter",
        side_effect=[
            Person(id=1, name="John Doe", age=30, gender="male", country="US")
        ],
    ):
        response = client.post("/v1/people/", json=people_data)

        mock_bulk_create.assert_called_once()

        assert response.status_code == 200
        assert response.json() == {
            "created_people": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "age": 30,
                    "gender": "male",
                    "country": "US",
                }
            ]
        }


@patch.object(
    SqlitePeopleRepository, "get_average_age_by_country", return_value=[("US", 27)]
)
def test_get_average_age(mock_get_average):
    """
    Test that the endpoint returns the correct average age by country
    when the SqlitePeopleRepository.get_average_age_by_country method is mocked
    """
    response = client.get("/v1/people/average/age")

    mock_get_average.assert_called_once()

    assert response.status_code == 200
    assert response.json() == [{"country": "US", "average_age": 27}]


@patch.object(
    SqlitePeopleRepository,
    "get_gender_repartition",
    return_value=[("female", 27), ("male", 7)],
)
def test_get_gender_repartition(mock_get_gender):
    """
    Test that the endpoint returns the correct format
    when the SqlitePeopleRepository.get_gender_repartition method is mocked
    """
    response = client.get("/v1/people/gender/")

    mock_get_gender.assert_called_once()

    assert response.status_code == 200
    assert response.json() == [
        {"gender": "female", "count": 27},
        {"gender": "male", "count": 7},
    ]


@patch.object(
    SqlitePeopleRepository,
    "get_number_for_country",
    return_value=[("US", 27), ("FR", 7)],
)
def test_get_number_of_people(mock_get_number):
    """
    Test that the endpoint returns the correct format
    when the SqlitePeopleRepository.get_number_for_country method is mocked
    """
    response = client.get("/v1/people/number")

    mock_get_number.assert_called_once()

    assert response.status_code == 200
    assert response.json() == [
        {"country": "US", "count": 27},
        {"country": "FR", "count": 7},
    ]
