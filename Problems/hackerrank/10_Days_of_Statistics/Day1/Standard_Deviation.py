# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - const
"""

import math

n = int(input())
x = list(map(int, input().split()))

mean = sum(x) / n

std = 0
for i in range(n):
    std += (x[i] - mean)**2 / n

print(round(float(math.sqrt(std)), 1))