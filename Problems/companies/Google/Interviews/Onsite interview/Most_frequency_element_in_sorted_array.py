"""
Find most frequent element in sorted array

"""


def most_frequent_num(nums):
    if not nums:
        return None

    cur_num, answer = nums[0], nums[0]
    count, max_count = 1, 1

    for num in nums[1:]:
        if cur_num == num:
            count += 1
        else:
            cur_num = num
            count = 1

        if max_count <= count:
            max_count = count
            answer = cur_num

    return answer


if __name__ == '__main__':
    nums = [1, 3, 3, 4, 4, 4, 5, 6, 6]

    print(most_frequent_num(nums))

