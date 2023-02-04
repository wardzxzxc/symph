from celery import Celery
from fastapi import APIRouter, Depends, HTTPException, status

from symph.routers import deps

router = APIRouter()


@router.get("/")
async def get_tasks_all_workers(celery_app: Celery = Depends(deps.get_celery_app)):
    """Get all tasks for all workers"""
    return celery_app.control.inspect(destination=None).registered()


@router.get("/{worker_name}")
async def get_tasks_by_worker_name(
    worker_name: str, celery_app: Celery = Depends(deps.get_celery_app)
):
    """Get all tasks given worker name"""
    tasks = celery_app.control.inspect(destination=[worker_name]).registered()
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return tasks
