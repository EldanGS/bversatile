# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem


def fact(n):
    result = 1
    for i in range(2, n):
        result *= i
    
    return result

def cnk(n, x):
    return fact(n) / (fact(x) * fact(n - x))

def b(x, n, p):
    return cnk(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
odds = l / r

print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))