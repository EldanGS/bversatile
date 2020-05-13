"""We are given an undirected graph that has characteristics of a k-ary tree.
In such a graph, we can choose any node as the root to make a k-ary tree. The
root (or the tree) with the minimum height will be called Minimum Height Tree
(MHT). There can be multiple MHTs for a graph. In this problem, we need to
find all those roots which give us MHTs. Write a method to find all MHTs of
the given graph and return a list of their roots.

Example 1:
Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the
height of the trees with roots '1' or '2' is three which is minimum.

Example 2:
Input: vertices: 4, Edges: [[0, 1], [0, 2], [2, 3]]
Output:[0, 2]
Explanation: Choosing '0' or '2' as roots give us MHTs. In the below diagram, we can see that the
height of the trees with roots '0' or '2' is three which is minimum.

Example 3:
Input: vertices: 4, Edges: [[0, 1], [1, 2], [1, 3]]
Output:[1]
"""

from collections import defaultdict


def find_trees(nodes, edges):
    """
    The time complexity of the below algorithm will be O(V+E), where ‘V’
    is the total nodes and ‘E’ is the total number of the edges.

    Space complexity # The space complexity will be O(V+E), since we are
    storing all of the edges for each node in an adjacency list.
    """
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        in_degree[u] += 1
        in_degree[v] += 1

    queue = [node for node in in_degree if in_degree[node] == 1]
    total_nodes = nodes
    while total_nodes > 2:
        leaf_nodes = len(queue)
        total_nodes -= leaf_nodes

        new_queue = []
        for node in queue:
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 1:
                    new_queue.append(child)
        queue = new_queue
    return queue


def main():
    print("Roots of MHTs: " +
          str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[1, 2], [1, 3]])))


main()
