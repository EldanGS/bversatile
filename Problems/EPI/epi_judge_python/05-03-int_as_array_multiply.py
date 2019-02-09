from test_framework import generic_test


def multiply(x, y):
    sign = -1 if ((x[0] < 0) ^ (y[0] < 0)) else 1
    x[0], y[0] = abs(x[0]), abs(y[0])

    n, m = len(x), len(y)
    result = [0] * (n + m)
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            result[i + j + 1] += x[i] * y[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("05-03-int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
