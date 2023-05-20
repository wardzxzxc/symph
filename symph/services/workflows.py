from typing import List

from .. import models


def generate_workflow(nodes: List[models.Node]):
    def dfs(node: models.Node):
        # when reach a leaf node
        if len(node.target_nodes()) == 0:
            return

    root_nodes = [n for n in nodes if len(n.source_nodes()) == 0]

    map(dfs, root_nodes)
