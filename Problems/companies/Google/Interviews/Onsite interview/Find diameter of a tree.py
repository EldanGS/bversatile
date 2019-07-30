"""
Find diameter of a tree

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionBTree:
    def __init__(self):
        self.result = 0

    def get_depth(self, node):
        if not node:
            return 0

        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)

        self.result = max(self.result, left_depth + right_depth)

        return max(left_depth, right_depth) + 1


    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.get_depth(root)
        return self.result


import collections


class SolutionDFS:
    def __init__(self, N, pairs):
        self.graph = collections.defaultdict(list)
        for u, v in pairs:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.height = [0] * N

    def get_height(self, node, parent):
        for to in self.graph[node]:
            if to == parent:
                continue
            self.height[node] = max(self.height[node], self.get_height(to, node))

        self.height[node] += 1

        return self.height[node]

    def diameter(self, node, parent):
        max1 = max2 = max_subtree = float('-inf')
        for to in self.graph[node]:
            if to == parent:
                continue

            if max1 < self.height[to]:
                max2 = max1
                max1 = self.height[to]
            else:
                max2 = self.height[to]

        for to in self.graph[node]:
            if to == parent:
                continue
            max_subtree = max(max_subtree, self.diameter(to, node))

        return max(max_subtree, max1 + max2 + 1)


class SolutionBFS:
    def __init__(self, N, pairs):
        self.graph = collections.defaultdict(list)
        for u, v in pairs:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.N = N

    def bfs(self, root):
        dist = [0] * self.N
        dist[root] = 1
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            for to in self.graph[node]:
                if dist[to] != 0:
                    continue
                queue.append(to)
                dist[to] = dist[node] + 1

        max_dist, vertex = float('-inf'), -1
        for i in range(self.N):
            if max_dist < dist[i]:
                max_dist = dist[i]
                vertex = i

        return (max_dist, vertex)

    def diameter(self, root):
        pair1 = self.bfs(root)
        pair2 = self.bfs(pair1[1])
        return pair2[0]


if __name__ == '__main__':
    pairs = [[0, 1], [0, 2], [1, 3]]
    n = len(pairs)

    dfs = SolutionDFS(n + 1, pairs)
    dfs.get_height(0, -1)
    print(dfs.diameter(0, -1))

    bfs = SolutionBFS(n + 1, pairs)
    print(dfs.diameter(0, -1))
