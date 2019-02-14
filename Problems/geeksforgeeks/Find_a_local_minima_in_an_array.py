# https://www.geeksforgeeks.org/find-local-minima-array/


# O(N) time, O(1) space
def find_local_minimum2(arr):
    if len(arr) < 2:
        return 1

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return i

    return len(arr) - 1


def find_local_minimum(arr):
    def binary_search(left, right, n):
        mid = (left + right) // 2

        if (mid == 0 or arr[mid - 1] > arr[mid]) and (mid == n - 1 or arr[mid] < arr[mid + 1]):
            return mid

        if mid > 0 and arr[mid - 1] < arr[mid]:
            return binary_search(left, mid - 1, n)
        return binary_search(mid + 1, right, n)

    return binary_search(0, len(arr) - 1, len(arr))


if __name__ == '__main__':
    arr = [9, 6, 3, 14, 5, 7, 4]
    # arr = [23, 8, 15, 2, 3]
    # arr = [1, 2, 3]
    # arr = [3, 2, 1]
    print(find_local_minimum(arr), find_local_minimum2(arr))
