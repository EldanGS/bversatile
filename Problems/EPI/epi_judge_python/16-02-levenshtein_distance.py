from test_framework import generic_test


def levenshtein_distance(A, B):
    if len(A) > len(B):
        A, B = B, A

    n, m = len(A) + 1, len(B) + 1
    distance = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[i][j] = i
            elif A[i - 1] == B[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = min(distance[i - 1][j], distance[i][j - 1], distance[i - 1][j - 1]) + 1

    return distance[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("16-02-levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
