from fastapi import APIRouter

from . import _workers

api_router = APIRouter()

api_router.include_router(_workers.router, prefix="/workers", tags=["workers"])
