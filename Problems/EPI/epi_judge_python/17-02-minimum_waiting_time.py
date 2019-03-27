from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    service_times.sort()
    total_waiting_time = 0

    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    return total_waiting_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-02-minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
