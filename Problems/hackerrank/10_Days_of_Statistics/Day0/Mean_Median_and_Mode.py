# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

n = int(input())
x = [int(x) for x in input().split()]

x.sort()

# mean/average
print(sum(x) / n)

# median
if n & 1:
    print(x[n - 1])
else:
    print((x[n // 2] + x[n // 2 - 1]) / 2)

# mode
max_count, current_count = 0, 1
mode = x[0]
for i in range(n - 1):
    if x[i] == x[i + 1]:
        current_count += 1
    else:
        if max_count < current_count:
            max_count = current_count
            mode = x[i]
        
        current_count = 1

print(mode)