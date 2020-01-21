"""
https://www.glassdoor.com/Interview/LinkedIn-Machine-Learning-Interview-Questions-EI_IE34865.0,8_KO9,25.htm#InterviewReview_30857461

Data Mining: given a function that returns a 0 with probability p and 1 with probability (1-p), create a function that returns 1 and 0 with 0.5 probability each.

Solution:
We know foo() returns 0 with 60% probability. How can we ensure that 0 and 1 are returned with 50% probability?
The solution is similar to this post. If we can somehow get two cases with equal probability, then we are done. We call foo() two times. Both calls will return 0 with 60% probability. So the two pairs (0, 1) and (1, 0) will be generated with equal probability from two calls of foo(). Let us see how.

(0, 1): The probability to get 0 followed by 1 from two calls of foo() = 0.6 * 0.4 = 0.24
(1, 0): The probability to get 1 followed by 0 from two calls of foo() = 0.4 * 0.6 = 0.24



DS/A: Given two sorted lists, create functions that would perform a set union and set intersections on the lists

"""


# returns a 0 with probability P
def given_func():
    pass


def make_fair_coin_from_biased_coin():
    val1 = given_func()
    val2 = given_func()

    # q = 1 - p

    # will reach with probability (p * q), 1 variant
    if val1 == 0 and val2 == 1:
        return 0

    # will reach with probability (p * q), 2 variant
    if val1 == 1 and val2 == 0:
        return 1

    # given 2 variants has the same probability.

    # will reach here with (1 - variant1 - variant2) = (1 - 2(p * q))
    return make_fair_coin_from_biased_coin()


def get_intersection_of_sorted_lists(l1: list, l2: list) -> list:
    n, m = len(l1), len(l2)
    intersections = []
    i, j = 0, 0

    while i < n and j < m:
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            if not intersections or intersections[-1] != l1[i]:
                intersections.append(l1[i])
            i, j = i + 1, j + 1

    return intersections


def get_union_of_sorted_list(l1: list, l2: list) -> list:
    n, m = len(l1), len(l2)
    union = []
    i, j = 0, 0

    while i < n and j < m:
        if l1[i] < l2[j]:
            union.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            union.append(l2[j])
            j += 1
        else:
            union.append(l1[i])
            i, j = i + 1, j + 1

    union.extend(l1[i:])
    union.extend(l2[j:])
    return union


if __name__ == '__main__':
    l1 = [1, 3, 3, 4, 5, 7]
    l2 = [2, 3, 5, 6]

    print('First list:', l1)
    print('Second list:', l2)
    print('Intersection:', get_intersection_of_sorted_lists(l1, l2))
    print('Union:', get_union_of_sorted_list(l1, l2))
