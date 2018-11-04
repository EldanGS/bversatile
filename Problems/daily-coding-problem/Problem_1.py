"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

"""
Solution.
Complexity analysis:
Time: O(N) - in worst case
Memory: O(N) - in worst case
"""


def find_target(A, target):
    data = {}
    for num in A:
        temp = target - num
        if data.get(temp):
            return True

        data[num] = 1

    return False


if __name__ == '__main__':
    A = [10, 15, 3, 7]
    target = 17

    print(find_target(A, target))
