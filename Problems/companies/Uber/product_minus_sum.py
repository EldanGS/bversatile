"""
Given an integer N, need to calculate product of its digit and subtract from sum of digits
productOfDigits - sumOfDigits.

Example,
n = 42,
4*2 - (4+2) = 2

"""


def product_subtract_sum(N: int) -> int:
    if not N:
        return 0

    negative = 1 if N > 0 else -1
    total_product, total_sum = 1, 0
    while N != 0:
        num = N % 10
        total_product *= num
        total_sum += num
        N //= 10

    return total_product * negative - total_sum * negative
