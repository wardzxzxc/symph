from typing import List

from pydantic import BaseModel


class EdgeCreate(BaseModel):
    src_number: int
    target_number: int


class EdgesCreate(BaseModel):
    edges: List[EdgeCreate]
