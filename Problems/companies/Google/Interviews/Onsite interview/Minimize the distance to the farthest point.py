"""
https://leetcode.com/discuss/interview-question/285144/Google-interview-question-Minimize-the-distance-to-the-farthest-point

This question was asked in Google interview.

Assume you're looking to move, and have a set of amenities that you want to have easy access to from your new home.
You have found a neighborhood you like, each block of which has zero or more amenities.
How would you pick the block to live in such that the farthest distance to any amenity in your list is minimized?

For example, say your list contains {school, grocery}, and the blocks are as follows:
1: restaurant, grocery
2: movie theater
3: school
4:
5: school

The ideal choice would be block 2, such that the distances to the grocery and the nearest school are 1 each.
Living on block 1 or 3 would make one of the distances zero, but the other one 2.

I came up with a naive solution as shown in the pseudocode below:

max = minus infinity
min = plus infinity
for r in requirements:
  for i in blocks:
    for j in blocks:
      if j.amenities contains r:
        max = maximum {max, dist(i, j)}
    if max < min:
      live_at = i

If n is the number of blocks, the time complexity for this algorithm is O(n^2),
assuming the list of requirements is small compared to n. Can we do better?

"""


def minimum_distance(blocks, amenities):
    block, min_len = 0, float('inf')
    window = {}

    low, high = 0, 0
    while high < len(blocks):
        add_block_to_window(blocks[high], amenities, window)
        while len(window) == len(amenities):
            cur_len = high - low
            if min_len > cur_len:
                min_len = cur_len
                block = (low + high) // 2 + 1

            remove_block_from_window(blocks[low], amenities, window)
            low += 1
        high += 1

    return block


def add_block_to_window(block, amenities, window):
    for amenity in block:
        if amenity in amenities:
            window[amenity] = window.get(amenity, 0) + 1


def remove_block_from_window(block, amenities, window):
    for amenity in block:
        if amenity in amenities:
            window[amenity] -= 1
            if window[amenity] == 0:
                del window[amenity]


def test(blocks, amenities, expected):
    actual = minimum_distance(blocks, amenities)

    assert expected == actual, 'Incorrect answer'
    return True


if __name__ == '__main__':
    # test 1
    blocks = [['restaurant', 'grocery'], ['movie theater'], ['school'], [''], ['school']]
    amenities = {'school', 'grocery'}
    expected = 2

    if test(blocks, amenities, expected):
        print('Correct')

    # test 2
    blocks = [['grocery'], ['movie theater'], ['school'], [''], ['school'], ['restaurant']]
    amenities = {'school', 'grocery', 'restaurant'}
    expected = 3

    if test(blocks, amenities, expected):
        print('Correct')
