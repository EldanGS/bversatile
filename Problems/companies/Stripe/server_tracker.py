"""
#
# You're running a pool of servers where the servers are
# numbered sequentially starting from 1. Over time, any
# given server might explode, in which case its server
# number is made available for reuse. When a new
# server is launched, it should be given the
# lowest available number.
#
# Write a function which, given the list of currently
# allocated server numbers, returns the number of the next server to allocate.

# For example, your function should behave something like the following:
#
#   >> next_server_number([5, 3, 1])
#   2
#   >> next_server_number([5, 4, 1, 2])
#   3
#   >> next_server_number([3, 2, 1])
#   4
#   >> next_server_number([2, 3])
#   1
#   >> next_server_number([])
#   1

# Server names consist of an alphabetic host type
# (e.g. "apibox") concatenated with the server number,
# with server numbers allocated as before (so "apibox1",
# "apibox2", etc. are valid hostnames).
#
# Write a name tracking class with two operations,
# allocate(host_type) and deallocate(hostname).
# The former should reserve and return the next
# available hostname, while the latter should release
# that hostname back into the pool.
#
# For example:
#
# >> tracker = Tracker.new()
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("apibox")
# "apibox2"
# >> tracker.deallocate("apibox1")
# nil
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("sitebox")
# "sitebox1"

"""

import collections


class Tracker:
    def __init__(self):
        self._tracker_map = collections.defaultdict(set)

    def allocate(self, hostname: str) -> str:
        next_num = self.next_server_num(self._tracker_map[hostname])
        self._tracker_map[hostname].add(next_num)
        return "{hostname}{number}".format(hostname=hostname, number=next_num)

    def deallocate(self, server: str) -> str:
        hostname, number = self.get_hostname_n_number(server)
        if not self.contain(hostname):
            raise KeyError

        self.remove_hostname_by_number(hostname, number)
        return "nil"

    def remove_hostname_by_number(self, hostname, number):
        self._tracker_map[hostname].remove(number)
        if not self._tracker_map[hostname]:
            del self._tracker_map[hostname]

    def contain(self, hostname):
        return hostname in self._tracker_map

    @staticmethod
    def get_hostname_n_number(server):
        for i, c in enumerate(server):
            if c.isdigit():
                return server[:i], int(server[i:])
        return server, 1

    @staticmethod
    def next_server_num(server_numbers):
        if not server_numbers:
            return 1
        else:
            for number in range(1, len(server_numbers) + 1):
                if number not in server_numbers:
                    return number
            return len(server_numbers) + 1


class TestTracker:
    def test_allocate(self):
        test_cases = [('allocate', 'apibox', 'apibox1'),
                      ('allocate', 'apibox', 'apibox2'),
                      ('allocate', 'apibox', 'apibox3'),
                      ('allocate', 'sitebox', 'sitebox1'),
                      ('allocate', 'sitebox', 'sitebox2')]
        self.tracker = Tracker()
        for func, hostname, expected in test_cases:
            actual = self.tracker.allocate(hostname)
            assert actual == expected, 'Unexpected result'

    def test_deallocate(self):
        test_cases = [('allocate', 'apibox', 'apibox1'),
                      ('allocate', 'apibox', 'apibox2'),
                      ('deallocate', 'apibox1', 'nil'),
                      ('allocate', 'sitebox', 'sitebox1'),
                      ('deallocate', 'sitebox', 'nil')]
        self.tracker = Tracker()
        for func, hostname, expected in test_cases:
            if func == 'allocate':
                self.tracker.allocate(hostname)
            else:
                actual = self.tracker.deallocate(hostname)
                assert actual == expected, 'Unexpected result'


if __name__ == '__main__':
    test_tracker = TestTracker()
    test_tracker.test_allocate()
