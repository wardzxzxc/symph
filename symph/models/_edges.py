from sqlalchemy import Column, ForeignKey, Integer, orm

from symph.database.base_class import Base

from ._nodes import Node


class Edge(Base):
    src_id = Column(Integer, ForeignKey("node.id"), primary_key=True)

    target_id = Column(Integer, ForeignKey("node.id"), primary_key=True)

    src_node = orm.relationship(
        Node, primaryjoin=src_id == Node.id, backref="source_edges"
    )

    target_node = orm.relationship(
        Node, primaryjoin=target_id == Node.id, backref="target_edges"
    )

    workflow_id = Column(Integer, ForeignKey("workflow.id"))

    def __init__(self, src_node: Node, target_node: Node):
        self.src_node = src_node
        self.target_node = target_node
