from test_framework import generic_test


def evaluate(expression):
    data = []
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }

    for token in expression.split(','):
        if token in OPERATORS:
            data.append(OPERATORS[token](data.pop(), data.pop()))
        else:
            data.append(int(token))

    return data[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("8-02-evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
