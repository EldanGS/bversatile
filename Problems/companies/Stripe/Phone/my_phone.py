#
# Your previous Plain Text content is preserved below:
#
# For this interview, imagine that we are working with a simple database. Each row
# associates column names (strings) with integer values (for example: 5, 0, -3,
# and so on). Here's a table with three rows:
#
#  a   b   c   d
# ---------------
#  1   0   0   0
#  0   2   3   0
#  0   0   0   4
#
# We can choose to represent a database table in JSON as an array of objects. For
# example, the previous table could be written as:
#
# [ {"a": 1, "b": 0, "c": 0, "d": 0},
#   {"a": 0, "b": 2, "c": 3, "d": 0},
#   {"a": 0, "b": 0, "c": 0, "d": 4} ]
#
# (There is no need to use JSON in your solutions -- the notation is just used to
# introduce and explain the problems.)
#
# Write a function minByColumn that takes a database table (as above), along with a
# column, and returns the row that contains the minimum value for the given column.
# If a row doesn't have any value for the column, your function should behave as
# though the value for that column was zero.
#
# In addition to writing this function, you should use tests to demonstrate that it's
# correct, either via an existing testing system or one you create.
#
# ## Examples
#
# table1 = [
#   {"a": 1},
#   {"a": 2},
#   {"a": 3}
# ]
# minByColumn(table1, "a") returns {"a": 1}
#
# table2 = [
#   {"a": 1, "b": 2},
#   {"a": 3, "b": 0}
# ]
# minByColumn(table2, "b") returns {"a": 3, "b": 0}
#
# table3 = [
#   {"a": 1, "b": -2},
#   {"a": 3}
# ]
# minByColumn(table3, "b") returns {"a": 1, "b": -2}
#
#
# table1 = [
#   {"a": 1},
#   {"a": 2},
#   {"a": 3}
# ]
# minByColumn(table1, "b") returns {"a": 1}
#
# table = []
#
#
#

import unittest


class DataBase:

    def exist_table(self, table):
        return table

    def row_consist(self, row, target):
        return target in row

    def min_by_column(self, table: list, target: str) -> dict:
        if not self.exist_table(table):
            raise KeyError

        result, min_value = table[0], float('inf')
        for row in table:
            row_value = row.get(target, 0)

            if min_value > row_value:
                result = row
                min_value = row_value

        return result


class TestDataBase(unittest.TestCase):
    def test_min_by_column(self):
        test_cases = [([{"a": 1}, {"a": 2}, {"a": 3}], 'a', {"a": 1}),
                      ([{"a": 1, "b": 2}, {"a": 3, "b": 0}], 'b',
                       {"a": 3, "b": 0}),
                      ([{"a": 1, "b": -2}, {"a": 3}, {"b": -1}], 'b',
                       {"a": 1, "b": -2}),
                      ([{"a": 1}, {"a": 2}, {"a": 3}], 'b', {"a": 1}),
                      ([{"a": 1, 'b': 5}, {"a": 2}, {"a": 3}], 'b', {"a": 2})]

        data_base = DataBase()
        for table, target, expected in test_cases:
            actual = data_base.min_by_column(table, target)

            assert actual == expected, 'Wrong answer'
            print('Accepted')


if __name__ == '__main__':
    test_data_base = TestDataBase()
    test_data_base.test_min_by_column()



