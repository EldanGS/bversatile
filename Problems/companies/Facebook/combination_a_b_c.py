# https://www.careercup.com/question?id=6324318653382656
# https://www.geeksforgeeks.org/count-strings-can-formed-using-b-c-given-constraints/


# O(2^N)
def solution_naive(n, b=1, c=2):
    if b < 0 or c < 0:
        return 0
    if n == 0:
        return 1
    if b == c == 0:
        return 1

    result = solution_naive(n - 1, b, c)
    result += solution_naive(n - 1, b - 1, c)
    result += solution_naive(n - 1, b, c - 1)
    return result


# O(N)
"""
O(n) solution is provided.

We can divide strings in two types;
A type which does not contain ‘b’
and B type which contain ‘b’.
We can define matrix A and B as follows.

A[i]: the number of strings of length i in A type.
B[i]: the number of strings of length i in B type.

And the answer is A[n] + B[n]

Because B type strings with lengh i can be generated 
by picking any sting in A type strings with length i-1,
and put ‘b’ in any position in the string.
There are total i positions to insert ‘b’,
thus, following equation holds between A[i] and B[i].

B[i] = i * A[i-1]

So, it is enough to compute A[i].
For considering strings in A, there are three possible 
prefixes which end with ‘a’.
(because there is no constraint in the substring after ‘a’)

1. ‘a’ + A type strings with length i - 1
2. ‘ca’ + A type strings with length i - 2
3. ‘cca’ + A type strings with length i - 3

i.e., A[i] = A[i-1] + A[i-2] + A[i-3]
where A[1] = 2, A[2] = 4, A[3] = 7

We can compute matrix A iteratively.

As an example, the number of strings of length 3 is
A[3] + B[3] = A[3] + 3 * A[2] = 7 + 3*4 = 19.
"""
def solution_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n] + n * dp[n - 1]


# O(1)
def solution_math(n):
    # 1 is all A's
    # (n * 2) is consecutive A with B and A with C
    # (n * n - 1) is sequence of A, B and C
    # n * (n * n - 1) means for n position used previous sequence
    # last // 2 means removed copies
    return 1 + (n * 2) + (n * (n * n - 1) // 2)


if __name__ == '__main__':
    n = 3

    result1 = solution_naive(n)
    result2 = solution_dp(n)
    result3 = solution_math(n)

    print(result1, result2, result3)
