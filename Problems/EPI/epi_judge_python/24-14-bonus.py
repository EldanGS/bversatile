from test_framework import generic_test
import heapq


def calculate_bonus(productivity):
    tickets = [1] * len(productivity)
    for i in range(1, len(productivity)):
        if productivity[i] > productivity[i - 1]:
            tickets[i] = tickets[i - 1] + 1

    for i in reversed(range(len(productivity) - 1)):
        if productivity[i] > productivity[i + 1]:
            tickets[i] = max(tickets[i], tickets[i + 1] + 1)

    return sum(tickets)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("24-14-bonus.py", 'bonus.tsv',
                                       calculate_bonus))
