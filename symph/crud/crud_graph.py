from typing import List

from sqlalchemy import orm

from symph.schemas import EdgesCreate, NodesCreate

from ._base import CRUDBase


class CRUDGraph:
    def __init__(self, crud_nodes: CRUDBase, crud_edges: CRUDBase):
        self._crud_nodes = crud_nodes
        self._crud_edges = crud_edges

    def create(
        self, s: orm.Session, *, nodes: List[NodesCreate], edges: List[EdgesCreate]
    ):
        self._crud_nodes.create_multi(s, list_objs=nodes)
        self._crud_edges.create_multi(s, list_objs=edges)
