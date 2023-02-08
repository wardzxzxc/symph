from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy import orm

from symph import crud, schemas
from symph.routers import deps

router = APIRouter()


@router.post("/{worker_name}", status_code=status.HTTP_201_CREATED)
def create_workflow_for_worker(
    nodes: List[schemas.NodeCreate],
    edges: List[schemas.EdgeCreate],
    s: orm.Session = Depends(deps.get_db),
):
    crud.graph.create(s, nodes=nodes, edges=edges)
    return "workflow created"
