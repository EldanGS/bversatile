# https://www.hackerrank.com/challenges/s10-quartiles/problem

n = int(input())
x = sorted(map(int, input().split()))

def median(nums):
    if len(nums) & 1:
        return nums[len(nums) // 2]
    else:
        return sum(nums[len(nums) // 2 - 1: len(nums) // 2 + 1]) // 2

def quartiles(n, nums):
    Q1 = median(nums[:n // 2])
    Q2 = median(nums)
    if n & 1:
        Q3 = median(nums[n // 2 + 1:])
    else:
        Q3 = median(nums[n // 2:])
    
    return Q1, Q2, Q3

Q1, Q2, Q3 = quartiles(n, x)

print(Q1)
print(Q2)
print(Q3)

