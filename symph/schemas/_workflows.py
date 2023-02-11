from typing import List

from pydantic import BaseModel

from ._edges import EdgeCreate
from ._nodes import NodeCreate


class WorkflowCreate(BaseModel):
    name: str
    nodes: List[NodeCreate]
    edges: List[EdgeCreate]
