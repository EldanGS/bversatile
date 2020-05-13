"""There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs, write a method to
find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5]
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]

"""

from collections import defaultdict, deque


def find_order(tasks, prerequisites):
    graph = defaultdict(list)
    in_degree = {task: 0 for task in range(tasks)}
    for task, pre in prerequisites:
        graph[task].append(pre)
        in_degree[pre] += 1

    queue = deque([task for task in range(tasks) if in_degree[task] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return sorted_order if len(sorted_order) == tasks else []


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
