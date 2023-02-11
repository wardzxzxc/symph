from sqlalchemy.orm import declarative_base

Base = declarative_base()

from ._edges import Edge  # noqa
from ._nodes import Node  # noqa
from ._workflows import Workflow  # noqa
