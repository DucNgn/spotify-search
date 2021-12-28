from fastapi import APIRouter

from .music import search_router

v1_router = APIRouter(prefix="/api/v1", responses={"404": {"description": "Not found"}})
v1_router.include_router(search_router)
