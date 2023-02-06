from sqlalchemy import Column, ForeignKey, Integer, orm

from . import Base
from .nodes import Node


class Edge(Base):
    __tablename__ = "edges"

    src_id = Column(Integer, ForeignKey("nodes.id"), primary_key=True)

    target_id = Column(Integer, ForeignKey("nodes.id"), primary_key=True)

    src_node = orm.relationship(
        Node, primaryjoin=src_id == Node.id, backref="source_edges"
    )

    target_node = orm.relationship(
        Node, primaryjoin=target_id == Node.id, backref="target_edges"
    )
