import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import deque


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []


def is_any_placement_feasible(graph):
    def bfs(node):
        node.d = 0
        queue = deque([node])

        while queue:
            vertex = queue.popleft()
            for edge in vertex.edges:
                if edge.d == -1:
                    edge.d = vertex.d + 1
                    queue.append(edge)
                elif edge.d == vertex.d:
                    return False

        return True

    return all(bfs(node) for node in graph if node.d == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("18-06-is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
