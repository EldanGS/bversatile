# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

"""
Solution.
Complexity analysis:
Time: O(NlogN) - always
Memory: O(N) - in worst case
"""

from statistics import median

n = int(input())
x = list(map(int, input().split()))
freq = list(map(int, input().split()))

data = []

for i in range(n):
    data += [x[i]] * freq[i]
    
N = sum(freq)
data.sort()

if n & 1:
    q1 = median(data[:N // 2])
    q3 = median(data[N // 2 + 1:])
else:
    q1 = median(data[:N // 2])
    q3 = median(data[N // 2:])

print(round(float(q3 - q1), 1))

