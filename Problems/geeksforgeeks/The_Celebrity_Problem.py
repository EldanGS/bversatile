# https://www.geeksforgeeks.org/the-celebrity-problem/

matrix = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]


def knows(a, b):
    return matrix[a][b]


def find_celebrity(n):
    a, b = 0, n - 1

    while a < b:
        if knows(a, b):
            a += 1
        else:
            b -= 1

    for i in range(n):
        if i != a and (knows(a, i) or not knows(i, a)):
            return -1

    return a


if __name__ == '__main__':
    n = 4
    celebrity = find_celebrity(n)

    if celebrity == -1:
        print('No celebrity')
    else:
        print('Celebrity:', celebrity)
