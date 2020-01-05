"""
https://leetcode.com/problems/factor-combinations/

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

"""


class Solution:

    def factors_generator(self, start, n, dividers, result):
        for divider in range(start, int(n ** 0.5) + 1):
            if n % divider == 0:
                dividers.append(divider)
                self.factors_generator(divider, n // divider, dividers, result)
                result.append(dividers + [n // divider])
                dividers.pop()

    def get_factors(self, n: int) -> list:
        result = []

        self.factors_generator(2, n, [], result)
        return result
