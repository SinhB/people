from os import getenv

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Store values we want to keep configurable
    """

    SQLITE_URL: str
    SQLITE_TEST_URL: str
    SQLITE_HOST: str


def load_config_from_env() -> Settings:
    config = Settings(
        SQLITE_URL=getenv("SQLITE_URL", default="sqlite+aiosqlite:///people.db"),
        SQLITE_TEST_URL=getenv(
            "SQLITE_TEST_URL", default="sqlite+aiosqlite:///:memory:"
        ),
        SQLITE_HOST=getenv("SQLITE_HOST", default="sqlite3"),
    )
    return config


settings = load_config_from_env()
