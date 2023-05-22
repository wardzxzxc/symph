from sqlalchemy import Column, ForeignKey, Integer, String

from symph.database.base_class import Base


class Node(Base):

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    workflow_id = Column(Integer, ForeignKey("workflow.id"))

    def source_nodes(self):
        return [x.src_node if x else x for x in self.target_edges]

    def target_nodes(self):
        return [x.target_node if x else x for x in self.source_edges]
