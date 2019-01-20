import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges = []


def is_deadlocked(graph):
    def has_cycle(cur):
        if cur.color == GraphVertex.GRAY:
            return True
        cur.color = GraphVertex.GRAY
        if any(next.color != GraphVertex.BLACK and has_cycle(next) for next in cur.edges):
            return True
        cur.color = GraphVertex.BLACK
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex)
               for vertex in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("18-04-deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
