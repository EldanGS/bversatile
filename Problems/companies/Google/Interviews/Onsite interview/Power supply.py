"""
https://leetcode.com/discuss/interview-question/321507/Google-or-Onsite-interview-or-Power-supply

I interviewed at Google for L3 few months back. I was asked this question that i couldn't figure out.
Let me know if anyone can figure out solution.

There are N cites (1,2,3,.....,N). For each city i, you can either create a power house or connect it through a wire to other city that has power.
You're given a cost array (Pi) of building a power house at i'th city, and cost matrix Ci-j of connecting wire to other cities.
You've to find minimum cost, such that each city will have power supply.


https://leetcode.com/discuss/interview-question/265623/Google-or-Phone-screen-or-Water-supply
Question 2:
Let's say you're an environmental engineer trying to assist in laying out infrastructure in some village.
The village has N houses, each which needs a water supply. A house can receive water if:

A well is built there
There is some path of pipes to a house with a water well
You work with a contractor and figure out

The cost to build a well at house (well_cost[i])
The cost of the pipe to connect house[i] and house[j] (pipe_cost[i][j])
What's the cheapest way to make sure every house in the village is connected to a water supply?

"""


class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]

    def get(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.get(self.parent[v])

        return self.parent[v]

    def union(self, u, v):
        parent_u = self.get(u)
        parent_v = self.get(v)

        if parent_u != parent_v:
            self.parent[parent_u] = self.parent[parent_v]


def water_supply(houses, costs):
    graph = []
    for cost, (u, v) in zip(costs, houses):
        graph.append((cost, u, v))

    graph.sort()

    n, total_min_cost = len(houses), 0
    path = []
    dsu = DSU(n)

    for cost, u, v in graph:
        if dsu.get(u) != dsu.get(v):
            path.append((u, v))
            total_min_cost += cost
            dsu.union(u, v)

    return total_min_cost, path


if __name__ == '__main__':
    #           5      100      20      70      9       17
    houses = [[0, 1], [0, 4], [1, 4], [1, 3], [3, 2], [4, 2]]
    costs  = [5, 100, 20, 70, 9, 17]

    expected = 51
    actual, path = water_supply(houses, costs)

    assert expected == actual, 'Incorrect'
    print('Correct')
    print('Path:', path)



