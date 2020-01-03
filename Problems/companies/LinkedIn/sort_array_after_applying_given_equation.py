"""
https://www.geeksforgeeks.org/sort-array-applying-given-equation/

We have an integer array that is sorted in ascending order. We also have 3 integers A, B and C.
We need to apply A*x*x + B*x + C for each element x in the array and sort the modified array.

Example:
Input : arr[] = {-1, 0, 1, 2, 3, 4}
       A = -1, B = 2, C = -1
Output : {-9, -4, -4, -1, -1, 0}
Input array is {-1, 0, 1, 2, 3, 4}.
After
applying the equation A*x*x + B*x + C on
every element x we get, {-4,-1, 0, -1, -4, -9}
After sorting, we get {-9, -4, -4, -1, -1, 0}

"""


def func(x, a, b, c):
    return a * x ** 2 + b * x + c


# O(NlogN) time, O(N) space
def sort_array_with_apply_func(nums: list, a: float, b: float, c: float):
    return sorted([func(x, a, b, c) for x in nums])


# O(N) time, O(N) space
def sort_array_with_apply_func2(nums: list, a: float, b: float, c: float):
    nums = [func(x, a, b, c) for x in nums]
    index, max_val = -1, float('-inf')
    for i, num in enumerate(nums):
        if max_val < num:
            index = i
            max_val = num

    n = len(nums)
    i, j, k = 0, n - 1, 0
    result = [0] * n
    while i < index < j:
        if nums[i] < nums[j]:
            result[k] = nums[i]
            i += 1
        else:
            result[k] = nums[j]
            j -= 1
        k += 1

    while i < index:
        result[k] = nums[i]
        i, k = i + 1, k + 1
    while j > index:
        result[k] = nums[j]
        j, k = j - 1, k + 1

    return result


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, 3, 4]
    A = -1
    B = 2
    C = -1
    print(sort_array_with_apply_func(arr, A, B, C))
    print(sort_array_with_apply_func2(arr, A, B, C))
