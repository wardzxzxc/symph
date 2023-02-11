from fastapi import APIRouter, Depends, status
from sqlalchemy import orm

from symph import crud, schemas
from symph.routers import deps

router = APIRouter()


@router.post("/{worker_name}", status_code=status.HTTP_201_CREATED)
def create_workflow_for_worker(
    workflow: schemas.WorkflowCreate,
    s: orm.Session = Depends(deps.get_db),
):
    crud.workflows.create(s, obj_in=workflow)
    return "workflow created"
