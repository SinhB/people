from people.core.dependencies import use_database
from people.infrastructure.repositories.people import SqlitePeopleRepository


async def get_people_repository():
    """
    Dependency factory function that creates an instance of the
    PeopleRepository using an async session.
    This function is used by FastAPI's dependency injection to provide
    the repository as a parameter in endpoint functions.

    Returns:
        PeopleRepository: An instance of the people repository
        with an open async session.
    """
    async with use_database() as session:
        repository = SqlitePeopleRepository(database_session=session)
        yield repository
