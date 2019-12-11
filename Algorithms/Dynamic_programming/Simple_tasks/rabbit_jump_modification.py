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


Now Rabbit not just jump into i'th stairs, now if i'th stairs is divisible to jump number.
"""


def number_of_steps(N, K):
    dp = [1] + [0] * N
    for i in range(2, N + 1):
        for j in range(K + 1):
            if i % j == 0:
                dp[i] += dp[i // j]
    return dp[-1]
