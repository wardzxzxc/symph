from sqlalchemy import Column, ForeignKey, Integer, String

from . import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    workflow_id = Column(Integer, ForeignKey("workflows.id"))

    def source_nodes(self):
        return [x.src_number for x in self.source_edges]

    def target_nodes(self):
        return [x.targert_id for x in self.target_edges]
