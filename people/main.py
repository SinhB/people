import uvicorn
from fastapi import FastAPI
from people.api.v1 import router
from people.core.database import engine

from people.models.people import Base


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = create_application()


@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
