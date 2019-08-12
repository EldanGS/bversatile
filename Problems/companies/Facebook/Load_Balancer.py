# https://www.lintcode.com/problem/load-balancer/description

"""
Description
Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.
"""

import random


class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.server = {}
        self.entity = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        # write your code here
        index = len(self.entity)
        self.server[server_id] = index
        self.entity.append(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        # write your code here
        index = self.server.get(server_id, -1)

        if index == -1:
            raise IndexError('{}, doesnt exist'.format(server_id))

        n = len(self.entity)
        self.entity[index] = self.entity[-1]
        self.server[self.entity[-1]] = index

        self.server.pop(server_id)
        del self.entity[-1]

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        # write your code here
        n = len(self.entity)
        index = random.randint(0, n - 1)
        return self.entity[index]
