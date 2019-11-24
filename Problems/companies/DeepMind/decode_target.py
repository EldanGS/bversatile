#!/bin/python3
import os
from random import randint, random
import numpy as np


# Outline of noisy_xor function
#################################################
### noise_rate = 0.02
###
### def noisy_xor(x):
###     n = sum(2**i if random() < noise_rate else 0 for i in range(N))
###     return bin(x ^ TARGET ^ n).count('1')
#################################################

def get_noisy_xor(target, N):
    noise_rate = 0.02

    def noisy_xor(x):  # Noisy Xor Sum
        # noise vector n.
        vector = [2 ** i if random() < noise_rate else 0 for i in range(N)]
        n = sum(vector)
        return bin(x ^ target ^ n).count('1')

    return noisy_xor


#
# Complete the 'decode_target' function below.
#
# The function is expected to return an INTEGER (target value).
# The function accepts following parameters:
#  1. ANONYMOUS FUNCTION noisy_xor
#  2. INTEGER N (number of bits of target value)
#

"""
write a method
decode_target(noisy_xor, N) that takes an ANONYMOUS function, noisy_xor, N, the number of bits in the target.
decode_target should find and return secret integer target by calling the passed in noisy_xor function.
"""




'''
# First idea
# O(N * |bits|) time
def get_num_from_bin(bits):
    return sum(2 ** i for i, bit in enumerate(bits) if bit == 1)


# O(N*2^N) time
def generate_binary_nums(n, bits, i, numbers):
    if i == n:
        if bits[0] != 0:
            number = get_num_from_bin(bits[::-1])
            numbers.append(number)
        return

    bits[i] = 0
    generate_binary_nums(n, bits, i + 1, numbers)
    bits[i] = 1
    generate_binary_nums(n, bits, i + 1, numbers)


# We can find via that approach to generate all possible variation of nums.
N = 6
candidates = []
generate_binary_nums(N, [0] * N, 0, candidates)
print(candidates)
'''


# Mathematical way is shifting 1 to N position and get lowest candidate num
# after added N - 1 bits we can identify our highest candidate, and keep all number in that range into array

def get_possible_candidate(N):
    N -= 1
    lowest_num = 1 << N
    highest_num = (1 << N) ^ (lowest_num - 1)
    return [num for num in range(lowest_num, highest_num + 1)]


def decode_target(noisy_xor, N):
    candidates = get_possible_candidate(N)
    for candidate in candidates:
        if not noisy_xor(candidate):
            return candidate
    return 0


if __name__ == '__main__':
    noisy_xor = get_noisy_xor(5, 3)
    print(decode_target(noisy_xor, 3))
