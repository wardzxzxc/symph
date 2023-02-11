from typing import List

from pydantic import BaseModel


class EdgeCreate(BaseModel):
    src_key: int
    target_key: int


class EdgesCreate(BaseModel):
    edges: List[EdgeCreate]
