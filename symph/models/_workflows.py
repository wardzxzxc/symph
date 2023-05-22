from sqlalchemy import Column, Integer, String, orm

from symph.database.base_class import Base


class Workflow(Base):

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

    nodes = orm.relationship("Node", backref="workflow", cascade="all,delete-orphan")

    edges = orm.relationship("Edge", backref="workflow", cascade="all,delete-orphan")
