"""
One curious child has a set of N little bricks (5 ≤ N ≤ 500). From these
bricks he builds different staircases. Staircase consists of steps of
different sizes in a strictly descending order. It is not allowed for
staircase to have steps equal sizes. Every staircase consists of at least two
steps and each step contains at least one brick.

Your task is to write a program that reads the number N and writes the only
number Q — amount of different staircases that can be built from exactly N
bricks.

Input: Number N
Output: Number Q

"""


def count_staircases(N):
    dp = [1] + [0] * N
    for i in range(1, N + 1):
        for j in range(N, i - 1, -1):
            dp[j] += dp[j - i]
    return dp[-1]


if __name__ == '__main__':
    for n in range(10):
        print('n =', n, 'result =', count_staircases(n))