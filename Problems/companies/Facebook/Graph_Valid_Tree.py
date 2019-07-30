# https://www.lintcode.com/problem/graph-valid-tree/description

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""

import collections


def dfs(u, visited, graph):
    if u in visited:
        return

    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v, visited, graph)


def is_valid_tree(n, edges) -> bool:
    if len(edges) != n - 1:
        return False

    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    dfs(0, visited, graph)

    return len(visited) == n


if __name__ == '__main__':
    n, edges = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]

    if is_valid_tree(n, edges):
        print('Valid tree')
    else:
        print('Invalid tree')
