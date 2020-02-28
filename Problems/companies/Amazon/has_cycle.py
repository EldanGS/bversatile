from collections import defaultdict


def is_cycle_detected(v, parent, graph, visited):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            if is_cycle_detected(u, v, graph, visited):
                return True
        elif u != parent:
            return True
    return False


def has_cycle(connections):
    graph = defaultdict(list)

    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    for v in range(len(graph)):
        if v in visited:
            continue
        if is_cycle_detected(v, -1, graph, visited):
            return True
    return False


def acycle(v, parent, graph, visited):
    visited[v] = 1
    for u in graph[v]:
        if u not in visited:
            if not acycle(u, v, graph, visited):
                return False
        elif u != parent:
            return False
    return True


def graph_has_cycle(nodes, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # 0 - not visited, 1 - visiting, 2 - visited
    visited = defaultdict(int)

    for node in nodes:
        if node not in visited and not acycle(node, -1, graph, visited):
            return True
    return False


if __name__ == '__main__':
    connections = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]
    if has_cycle(connections):
        print('Cycle detected')
    else:
        print('No cycle')

    connections = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]
    nodes = [0, 1, 2, 3, 4]
    if graph_has_cycle(nodes, connections):
        print('Cycle detected')
    else:
        print('No cycle')