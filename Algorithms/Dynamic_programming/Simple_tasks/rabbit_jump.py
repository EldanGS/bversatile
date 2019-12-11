"""
There's a hare in our zoo. He was placed in a cage, and in order not to be
bored, the director of the zoo ordered to put a ladder in his cage. Now our
bunny can jump up the stairs, jumping over the stairs. The ladder has a
certain number of steps N. A rabbit can make a single jump through no more
than K steps. For a change, the hare tries to find a new path to the top of
the stairs each time. The director is curious how many different ways the
hare has to get to the top of the stairs at the given values of K and N. Help
the director write a program to help calculate this number. For example,
if K=3 and N=4, there are the following routes: 1+1+1+1+1, 1+1+2, 1+2+1,
2+1+1, 2+2, 1+3, 3+1. That is, with these values the hare has only 7
different routes to get to the top of the stairs.


Input data

The only line of the INPUT.TXT input file contains two natural numbers K and
N (1 ≤ K ≤ N ≤ 300). K - the maximum number of steps that can be overcome by
a single jump, N - the total number of steps in the staircase.

Output data

The only line of the output file OUTPUT.TXT should display the number of
possible options for different routes of the hare on the top step of the
stairs without leading zeros.

Examples

input    ; output:
K=1, N=3 ; 1
K=2, N=7 ; 21
K=3 N=10 ; 274

"""


def number_of_steps(N, K):
    """
    The solution based on dynamic programming, for first K steps we should
    prepare count of possible moves. After next ith position we can calculate
    from sum(dp[i - 1], dp[i - 2], .., dp[i - k]) elements.

    recurrent formula:
    dp[i] = sum(dp[i - j]) for i in min(k, i) to n

    complexity: O(N * K) time, O(N) space
    """

    dp = [1] + [0] * N
    for i in range(1, N + 1):
        r = min(K, i)
        for j in range(1, r + 1):
            dp[i] += dp[i - j]

    return dp[-1]


def test_number_of_steps(N, K, expected):
    actual = number_of_steps(N, K)
    assert actual == expected, 'Wrong answer'


if __name__ == '__main__':
    N, K = 3, 1

    for K, N, expected in ((1, 3, 1), (2, 7, 21), (3, 10, 274)):
        test_number_of_steps(N, K, expected)
    print('Accepted')
