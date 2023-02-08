from typing import List

from pydantic import BaseModel


class NodeCreate(BaseModel):
    number: int
    name: str


class NodesCreate(BaseModel):
    nodes: List[NodeCreate]
