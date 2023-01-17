from typing import Any, Dict

from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from people.core.config import settings

engine = create_async_engine(settings.SQLITE_URL)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    def dict(self) -> Dict[str, Any]:
        dict_representation = {
            c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs
        }
        return dict_representation
