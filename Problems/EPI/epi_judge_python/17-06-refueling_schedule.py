import functools
import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    CityAndRemaining = collections.namedtuple('CityAndRemaining', ('city', 'remaining_gallons'))
    city_remaining_gallons_pair = CityAndRemaining(0, 0)
    remaining_gallons, num_cities = 0, len(gallons)

    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemaining(i, remaining_gallons)

    return city_remaining_gallons_pair.city


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-06-refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
