# https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram/0

def maximum_rectangular_area(A, n):
    if not A:
        return 0

    entities, max_rectangle = [], 0
    for i, h in enumerate(A + [0]):
        while entities and A[entities[-1]] >= h:
            height = A[entities.pop()]
            width = i if not entities else i - entities[-1] - 1
            max_rectangle = max(max_rectangle, height * width)

        entities.append(i)
    return max_rectangle


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(maximum_rectangular_area(A, N))
