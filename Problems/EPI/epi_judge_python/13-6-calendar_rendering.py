import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


# Author solution
def find_max_simultaneous_events1(A):
    E = [p for event in A for p in (Endpoint(event.start, True),
                                    Endpoint(event.finish, False))]
    E.sort(key=lambda e: (e.time, not e.is_start))
    max_parallel_num, parallel_num = 0, 0
    for e in E:
        if e.is_start:
            parallel_num += 1
            max_parallel_num = max(max_parallel_num, parallel_num)
        else:
            parallel_num -= 1

    return max_parallel_num


# My solution
def find_max_simultaneous_events(A):
    E = [(x[0], 1) for x in A] + [(x[1], -1) for x in A]
    E.sort(key=lambda x: (x[0], -x[1]))
    max_parallel_events, balance = 0, 0
    for e in E:
        balance += e[1]
        max_parallel_events = max(max_parallel_events, balance)

    return max_parallel_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("13-6-calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
