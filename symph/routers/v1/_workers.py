from fastapi import APIRouter, Depends

from symph.routers import deps

router = APIRouter()


@router.get("/")
def get_tasks_all_workers(inspector=Depends(deps.get_inspector)):
    return inspector.inspect("registered", None)


@router.get("/{worker_name}")
def get_tasks_by_worker_name(worker_name: str, inspector=Depends(deps.get_inspector)):
    return inspector.inspect("registered", [worker_name])
