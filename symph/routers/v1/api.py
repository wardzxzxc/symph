from fastapi import APIRouter

from . import _tasks

api_router = APIRouter()

api_router.include_router(_tasks.router, prefix="/tasks", tags=["tasks"])
