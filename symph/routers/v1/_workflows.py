from typing import Dict, List, Optional, Set

from celery import Celery
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import orm

from symph import crud, models, schemas, services
from symph.routers import deps

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_workflow_for_worker(
    worker_name: str,
    workflow: schemas.WorkflowCreate,
    s: orm.Session = Depends(deps.get_db),
    celery_app: Celery = Depends(deps.get_celery_app),
):
    distinct_nodes: Set[str] = set([node.name for node in workflow.nodes])
    worker_tasks: Optional[Dict[str, List[str]]] = celery_app.control.inspect(
        destination=[worker_name]
    ).registered()
    if worker_tasks is None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Worker not found"
        )
    all_tasks: List[str] = []
    for tasks in worker_tasks.values():
        all_tasks.extend(tasks)

    all_tasks: Set[str] = set(all_tasks)

    if len(all_tasks & distinct_nodes) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nodes contain tasks that does not belong to worker",
        )

    workflow: models.Workflow = crud.workflows.create(s, obj_in=workflow)

    return {"workflow_id": workflow.id, "message": "Workflow created"}


@router.post("/{worker-name}/{workflow-id}", status_code=status.HTTP_200_OK)
def start_workflow(
    worker_name: str,
    workflow_id: str,
    s: orm.Session = Depends(deps.get_db),
    celery_app: Celery = Depends(deps.get_celery_app),
):
    workflow = crud.workflows.get(s, id=workflow_id)
    workflow_builder = services.WorkflowBuilder(
        workflow_id=workflow.id, db_session=s, celery_app=celery_app
    )
    all_tasks = workflow_builder.build()
    print(all_tasks)
