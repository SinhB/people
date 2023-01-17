from fastapi import APIRouter

from people.api.v1.people import router as people_router

router = APIRouter(prefix="/v1")
router.include_router(people_router)
