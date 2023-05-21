from typing import List, Optional

from celery import Celery
from sqlalchemy import orm

from symph import crud, models


class WorkflowBuilder:
    def __init__(self, workflow_id: str, db_session: orm.Session, celery_app: Celery):
        self.workflow_id: str = workflow_id
        self.tasks: List[str] = []
        self.db_session: orm.Session = db_session
        self.celery_app: Celery = celery_app

    def build(self):
        db_obj: models.Workflow = crud.workflows.get(self.db_session, self.workflow_id)
        all_nodes: List[models.Node] = db_obj.nodes
        start_node: Optional[models.Node] = None
        for node in all_nodes:
            start_node = node if len(node.source_nodes()) == 0 else None
            break

        if not start_node:
            raise ValueError()

        curr: Optional[models.Node] = start_node

        while True:
            if not curr:
                # reach end of workflow
                break

            self.tasks.append((curr.name, curr.id))

            target_nodes: List[models.Node] = curr.target_nodes()

            curr = target_nodes[0] if len(target_nodes) != 0 else None

        return self.tasks
