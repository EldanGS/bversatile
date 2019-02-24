# https://www.geeksforgeeks.org/lexicographically-previous-permutation-in-c/


def prev_permutation(s):
    inversion_point = len(s) - 2

    while inversion_point >= 0 and s[inversion_point] <= s[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        return '-1'

    s = list(s)
    for i in reversed(range(inversion_point + 1, len(s))):
        if s[i] < s[inversion_point]:
            s[i], s[inversion_point] = s[inversion_point], s[i]
            break

    s[inversion_point + 1:] = reversed(s[inversion_point + 1:])
    return ''.join(s)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        print(prev_permutation(s))
