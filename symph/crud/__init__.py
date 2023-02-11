from symph.models import Edge, Node
from symph.schemas import EdgeCreate, NodeCreate

from ._base import CRUDBase
from ._workflows import CRUDWorkflows

nodes = CRUDBase[Node, NodeCreate](Node)
edges = CRUDBase[Edge, EdgeCreate](Edge)
workflows = CRUDWorkflows()
