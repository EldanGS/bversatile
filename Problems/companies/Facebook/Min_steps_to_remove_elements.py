# https://leetcode.com/discuss/interview-question/349687/Facebook-or-Onsite-or-Min-steps-to-remove-elements
"""
Given an array of numbers, remove the elements according to following conditions
    *remove an element arr[i] if and only if arr[i-1] < arr[i]

You might get the resulting array after removing the elements.
Repeat the process until array remains unchanged.
Return the number of steps in which the array remains unchanged.


Eg:
[6,3,1,8,9,4,3,2,8,9]

after 1st iteration we get

Step 1: [6,3,1,4,3,2] ---> [8,9] is removed since 1<8<9 && 2<8<9
Step 2: [6,3,1,3,2] ---> [4] is removed since 1<4
Step 3: [6,3,1,2] ---> [3] is removed since 1<3
Step 4: [6,3,1] ---> [2] is removed since 1<2

Answer: 4 (Total no. of steps are 4)

"""


def min_steps_to_remove_elements(nums):
    steps, stack = 0, []

    for i in reversed(range(len(nums))):
        if stack and nums[stack[-1]] > nums[i]:
            steps += 1
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

        stack.append(i)

    return steps


def _test(nums, expected):
    actual = min_steps_to_remove_elements(nums)

    assert actual == expected, 'Wrong answer: {}, {}'.format(actual, expected)
    print('Accepted')


if __name__ == '__main__':
    nums = [6, 3, 1, 8, 9, 4, 3, 2, 8, 9]
    _test(nums, 4)
