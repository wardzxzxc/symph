from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .edges import Edge  # noqa
from .nodes import Node  # noqa
from .workflows import Workflow  # noqa
