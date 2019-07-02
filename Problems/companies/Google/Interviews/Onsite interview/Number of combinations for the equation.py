"""
https://leetcode.com/discuss/interview-question/178793/Google-onsite-Number-of-combinations-for-the-equation

Given an array of Integers, find out how many combinations in the array,
satisfy the equation x+y+z=w, where x,y,z and w belong to the array and idx(x)<idx(y)<idx(z)<idx(w).
Elements are unique.

example :
input: [2,3,5,1,10] output: 1 {(2, 3, 5, 10)}
input: [4,6,9,3,13,18] output: 2{(4,6,3,13),(6,9,3,18)}

"""
from collections import namedtuple


def triplest_combination(nums):
    left_sum, right_sum = {}, {}
    result, n = [], len(nums)
    IndexAndNums = namedtuple('IndexAndNums', ('index', 'num1', 'num2'))

    for i in range(n):
        for j in range(i + 1, n):
            cur = nums[i] + nums[j]
            if cur in left_sum:
                left_sum[cur].append((IndexAndNums(j, nums[i], nums[j])))
            else:
                left_sum[cur] = [(IndexAndNums(j, nums[i], nums[j]))]

    for i in reversed(range(n)):
        for j in reversed(range(i)):
            cur = nums[i] - nums[j]
            if cur in right_sum:
                right_sum[cur].append((IndexAndNums(j, nums[i], nums[j])))
            else:
                right_sum[cur] = [(IndexAndNums(j, nums[i], nums[j]))]

    uniq_entity = left_sum.keys() & right_sum.keys()

    count = 0
    for key in uniq_entity:
        for left in left_sum[key]:
            for right in right_sum[key]:
                if left.index < right.index:
                    print("{}+{}+{}={}".format(left[1], left[2], right[2], right[1]))
                    count += 1

    return count


def test1():
    nums = [2,3,5,1,10]
    actual = triplest_combination(nums)
    expected = 1

    assert actual == expected, 'Incorrect answer'
    print('Correct answer')


if __name__ == '__main__':
    test1()