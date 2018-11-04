""""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""


def cons(a, b):
    return lambda f: f(a, b)


def car(f):
    return f(lambda a, b: a)


def cdr(f):
    return f(lambda a, b: b)


if __name__ == '__main__':
    print('Pair:', (3, 4))
    print('First element:', car(cons(3, 4)))
    print('Second element:', cdr(cons(3, 4)))
