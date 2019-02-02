from test_framework import generic_test


def evaluate(expression):
    DELIMETR = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }
    result = []
    for token in expression.split(DELIMETR):
        if token in OPERATORS:
            result.append(OPERATORS[token](result.pop(), result.pop()))
        else:
            result.append(int(token))

    return result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("08-02-evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
