# https://leetcode.com/problems/clone-graph/

import collections


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = collections.deque([node])
        vertex_map = {node: Node(node.val, [])}
        while queue:
            v = queue.popleft()

            for e in v.neighbors:
                if e not in vertex_map:
                    vertex_map[e] = Node(e.val, [])
                    queue.append(e)

                vertex_map[v].neighbors.append(vertex_map[e])

        return vertex_map[node]
