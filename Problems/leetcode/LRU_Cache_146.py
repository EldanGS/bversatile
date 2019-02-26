# https://leetcode.com/problems/lru-cache/

import collections


class LRUCache:

    def __init__(self, capacity: 'int'):
        self._cache_table = collections.OrderedDict()
        self._capacity = capacity

    def get(self, key: 'int') -> 'int':
        if key not in self._cache_table:
            return -1

        value = self._cache_table.pop(key)
        self._cache_table[key] = value

        return value

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self._cache_table:
            del self._cache_table[key]

        if len(self._cache_table) == self._capacity:
            self._cache_table.popitem(last=False)

        self._cache_table[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
