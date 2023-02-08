from sqlalchemy import Column, Integer, String

from . import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    def source_nodes(self):
        return [x.src_number for x in self.source_edges]

    def target_nodes(self):
        return [x.targert_id for x in self.target_edges]
