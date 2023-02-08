from fastapi import APIRouter

from . import _tasks, _workflows

api_router = APIRouter()

api_router.include_router(_tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(_workflows.router, prefix="/workflows", tags=["workflows"])
