"""
Your previous Plain Text content is preserved below :

* * # Step 1
Throughout this interview, we'll pretend we're building a new * analytical
database. Don't worry about actually building a database though – * these
will all be toy problems. * * Here's how the database works: all records are
represented as maps, with * string keys and integer values. The records are
contained in an array, in no * particular order. *

* To begin with, the database will support just one function: min_by_key.
This * function scans the array of records and returns the record that has
the * minimum value for a specified key. Records that do not contain the
specified * key are considered to have value 0 for the key. Note that keys
may map to * negative values! *

* Here's an example use case: each of your records contains data about a
school * student. You can use min_by_key to answer questions such as "who is
the * youngest student?" and "who is the student with the lowest grade-point
* average?" * * Implementation notes: You should handle an empty array of
records in an * idiomatic way in your language of choice. If several records
share the same * minimum value for the chosen key, you may return any of
them. * * ### Java function signature: ``` public static Map<String, Integer>
* minByKey(String key, List<Map<String, Integer>> records); ``` * *


### Examples (in Python): ```
assert min_by_key("a", [{"a": 1, "b": 2}, {"a": * 2}]) == {"a": 1, "b": 2}
assert min_by_key("a", [{"a": 2}, {"a": 1, "b": 2}]) * == {"a": 1, "b": 2}
assert min_by_key("b", [{"a": 1, "b": 2}, {"a": 2}]) == * {"a": 2}
assert min_by_key("a", [{}]) == {}
assert min_by_key("b", [{"a": * -1}, {"b": -1}]) == {"b": -1} ``` */



* * # Step 2: first_by_key Our next step in database development is to add a new
function. We'll call this function first_by_key. It has much in common with
min_by_key. first_by_key takes three arguments: a string key a string sort
direction (which must be either "asc" or "desc") an array of records, just as
in min_by_key. If the sort direction is "asc", then we should return the
minimum record, otherwise we should return the maximum record. As before,
records without a value for the key should be treated as having value 0. Once
you have a working solution, you should re-implement min_by_key in terms of
first_by_key .

"""


class DataBase:
    def min_by_key(self, target: str, data: list) -> dict:
        """
        Return first row which consist minimum value by target
        :param target: searching item
        :param data: collections data
        :return: dictionary
        """
        result, min_value = {}, float('inf')

        for row in data:
            if self.has_row(row, target):
                if min_value > row[target]:
                    min_value = row[target]
                    result = row
        return result

    def first_by_key(self, target: str, order: str, data: list) -> dict:
        result, min_value = {}, float('inf')

        for row in data:
            if self.has_row(row, target):
                if self.min_by_order(order, min_value, row[target]):
                    min_value = row[target]
                    result = row
        return result

    def min_by_order(self, order, min_value, current_value):
        if order == 'desc':
            return min_value >= current_value
        else:
            return min_value > current_value

    def has_row(self, row, target):
        return target in row


class TestDataBase:
    def test_data_to_min_by_key(self):
        test_cases = [("a", [{"a": 1, "b": 2}, {"a": 2}], {"a": 1, "b": 2}),
                      ("b", [{"a": 2}, {"a": 1, "b": 2}], {"a": 1, "b": 2}),
                      ("a", [{}], {}),
                      ("b", [{"a": -1}, {"b": -1}], {"b": -1})]

        for target, data, expected in test_cases:
            actual = DataBase().min_by_key(target, data)
            assert actual == expected, 'Unexpected result'

    def test_data_to_fist_by_key(self):
        test_cases = [("a", "asc", [{"a": 1}], {"a": 1}),
                      ("a", "desc", [{"a": 1}, {"a": 1, "b": 2}],
                       {"a": 1, "b": 2}),
                      ("a", "asc", [{"a": 1}, {"a": 1, "b": 2}],
                       {"a": 1}),
                      ("a", "desc", [{}], {}),
                      ("b", "asc", [{"a": -1}, {"b": -1}], {"b": -1})]

        for target, order, data, expected in test_cases:
            actual = DataBase().first_by_key(target, order, data)
            assert actual == expected, 'Unexpected result'


if __name__ == '__main__':
    test = TestDataBase()
    test.test_data_to_min_by_key()
