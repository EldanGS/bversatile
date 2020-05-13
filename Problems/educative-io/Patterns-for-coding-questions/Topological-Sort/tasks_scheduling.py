"""There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs, find out if it is
possible to schedule all the tasks.

Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]

Example 2:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.

Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible sceduling of tasks is: [0 1 4 3 2 5]
"""

from collections import defaultdict, deque

"""
Time complexity # In step ‘d’, each task can become a source only once and 
each edge (prerequisite) will be accessed and removed once. Therefore, 
the time complexity of the above algorithm will be O(V+E)O(V+E), where ‘V’ is 
the total number of tasks and ‘E’ is the total number of prerequisites. 

Space complexity # The space complexity will be O(V+E)O(V+E), ), since we are 
storing all of the prerequisites for each task in an adjacency list. 
"""
def is_scheduling_possible(tasks, prerequisites):
    graph = defaultdict(list)
    in_degree = {task: 0 for task in range(tasks)}
    for task, pre in prerequisites:
        graph[task].append(pre)
        in_degree[pre] += 1

    queue = deque([task for task in range(tasks) if in_degree[task] == 0])
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            return False
        visited.add(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return len(visited) == tasks


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
