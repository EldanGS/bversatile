# https://www.geeksforgeeks.org/minimum-flips-make-1s-left-0s-right-set-2/


def minimum_flips(S):
    n = len(S)
    flips_from_left, flips_from_right = [0] * n, [0] * n
    flips = 0
    for i in range(n):
        if S[i] == '0':
            flips += 1
        flips_from_left[i] = flips

    flips = 0
    for i in reversed(range(n)):
        if S[i] == '1':
            flips += 1
        flips_from_right[i] = flips

    min_flips = float('inf')
    for i in range(1, n):
        min_flips = min(min_flips, flips_from_left[i - 1] + flips_from_right[i])
        # print('i =', i, '| left flip', flips_from_left[i - 1], '| right flip', flips_from_right[i])
    return min_flips


if __name__ == '__main__':
    S = '101100'
    print('bits:', S, '| min flips:', minimum_flips(S))
