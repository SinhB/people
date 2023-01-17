from contextlib import asynccontextmanager

from people.core.database import SessionLocal


@asynccontextmanager
async def use_database():
    """
    A context manager function that manages the creation
    and closing of a database session.
    This function creates a new session using the `SessionLocal` class,
    and yields the session to the user.
    Once the user is done with the session, it is closed automatically.

    Usage:
    async with use_database() as session:
        # Use session to interact with the database
        ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
