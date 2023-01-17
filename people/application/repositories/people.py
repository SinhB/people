from abc import ABC, abstractmethod

from people.domain.entities import Person, PersonForm


class PeopleRepository(ABC):
    """
    People repository is the interface to interact with persistence
    when it comes to storing and retrieving data.
    """

    @abstractmethod
    async def bulk_create(self, people: list[PersonForm]) -> list[Person]:
        """
        Creates a list of people in the database.

        Parameters:
            people: A list of people to be created.

        Returns:
            A list of created people.
        """
        ...

    @abstractmethod
    async def get_average_age_by_country(self):
        """
        Retrieves the average age of people grouped by country.

        Returns:
            A list of tuples containing the country
            and its corresponding average age.
        """
        ...

    @abstractmethod
    async def get_number_for_country(self):
        """
        Retrieves the number of people for each country.

        Returns:
            A list of tuples containing the country
            and its corresponding number of people.
        """
        ...

    @abstractmethod
    async def get_gender_repartition(self, country: str):
        """
        Retrieves the gender repartition of people for a given country.

        Parameters:
            country: The country for which the gender repartition is retrieved.

        Returns:
            A list of tuples containing the gender
            and its corresponding number of people.
        """
        ...
