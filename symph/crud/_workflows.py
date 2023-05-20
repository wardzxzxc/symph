from typing import Dict, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import orm

from symph import models, schemas


class CRUDWorkflows:
    def __init__(self):
        self.model = models.Workflow

    def create(self, s: orm.Session, *, obj_in: schemas.WorkflowCreate):
        db_obj = self.model(name=obj_in.name)
        nodes: Dict[str, models.Node] = {}

        for n in obj_in.nodes:
            nodes[n.key] = models.Node(**jsonable_encoder(n))

        db_obj.nodes = [*nodes.values()]

        # link nodes via edges
        db_obj.edges = [
            models.Edge(nodes.get(e.src_key), nodes.get(e.target_key))
            for e in obj_in.edges
        ]

        s.add(db_obj)
        s.commit()
        s.refresh(db_obj)
        return db_obj

    def get(self, s: orm.Session, id: int) -> Optional[models.Workflow]:
        return s.query(self.model).filter(self.model.id == id).first()
