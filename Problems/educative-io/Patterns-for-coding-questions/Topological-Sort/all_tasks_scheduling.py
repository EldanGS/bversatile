"""There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs, write a method to
print all possible ordering of tasks meeting all prerequisites.

Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.

Example 2:
Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output:
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.

Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output:
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
"""

from collections import defaultdict, deque

"""If we don’t have any prerequisites, all combinations of the tasks can 
represent a topological ordering. As we know, that there can be N!N! 
combinations for ‘N’ numbers, therefore the time and space complexity of our 
algorithm will be O(V! * E), O(V! * E) where ‘V’ is the total number of tasks and 
‘E’ is the total prerequisites. We need the ‘E’ part because in each 
recursive call, at max, we remove (and add back) all the edges. """

def print_orders(tasks, prerequisites):
    graph = defaultdict(list)
    in_degree = {task: 0 for task in range(tasks)}
    for task, pre in prerequisites:
        graph[task].append(pre)
        in_degree[pre] += 1

    queue = deque([task for task in range(tasks) if in_degree[task] == 0])
    sorted_orders = []
    print_all_order(graph, in_degree, queue, sorted_orders, [])
    for num, order in enumerate(sorted_orders, 1):
        print("{}) {}".format(num, order))


def print_all_order(graph, in_degree, queue, sorted_orders, order):
    if queue:
        for v in queue:
            order.append(v)
            next_queue = deque(queue)
            next_queue.remove(v)
            for child in graph[v]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    next_queue.append(child)

            print_all_order(graph, in_degree, next_queue, sorted_orders, order)

            order.remove(v)
            for child in graph[v]:
                in_degree[child] += 1
    if len(order) == len(in_degree):
        sorted_orders.append(order[:])


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
