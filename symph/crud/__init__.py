from symph.models import Edge, Node
from symph.schemas import EdgeCreate, NodeCreate

from ._base import CRUDBase
from .crud_graph import CRUDGraph

nodes = CRUDBase[Node, NodeCreate](Node)
edges = CRUDBase[Edge, EdgeCreate](Edge)
graph = CRUDGraph(nodes, edges)
