# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

"""
Solution.
Complexity analysis:
Time: O(N) - always
Memory: O(1) - in worst case
"""

n = int(input())
x = [float(val) for val in input().split()]
w = [float(val) for val in input().split()]

total = 0
for i in range(n):
    total += x[i] * w[i]

print(round(total / sum(w), 1))
