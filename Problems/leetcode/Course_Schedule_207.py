# https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [-1] * numCourses  # -1 not visited, 0 visited, 1 leave

        for u, v in prerequisites:
            graph[u].append(v)

        def has_cycle(v):
            if visited[v] == 0:
                return True
            if visited[v] == 1:
                return False

            visited[v] = 0
            for u in graph[v]:
                if has_cycle(u):
                    return True

            visited[v] = 1
            return False

        for v in range(numCourses):
            if has_cycle(v):
                return False

        return True
