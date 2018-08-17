# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

def factorial(n):
    fact = 1
    for val in range(2, n + 1):
        fact *= val
    return fact

def Cnk(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))

def binom(x, n, p):
    return Cnk(n, x) * p**x * (1 - p)**(n - x)

l, r = list(map(float, input().split(' ')))
odds = l / r

print(round(sum([binom(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))