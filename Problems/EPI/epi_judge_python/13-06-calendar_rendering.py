import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    Events = [(x[0], 1) for x in A] + [(x[1], -1) for x in A]
    Events.sort(key=lambda x: (x[0], -x[1]))
    max_events = current_events = 0
    for event in Events:
        current_events += event[1]
        max_events = max(max_events, current_events)

    return max_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("13-06-calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
